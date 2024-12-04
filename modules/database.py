import sqlite3
import time
import os
import asyncio

db_connection = sqlite3.connect(os.path.join(os.path.dirname(os.path.dirname(__file__)), "bot.db"), check_same_thread=False, timeout=10)
db_cursor = db_connection.cursor()
create_statements = (
    '''
    CREATE TABLE IF NOT EXISTS channels (
        server_id TEXT, 
        channel_id TEXT, 
        history TEXT, 
        personality TEXT, 
        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    CREATE TABLE IF NOT EXISTS servers (
        server_id TEXT
    );
    CREATE TABLE IF NOT EXISTS users (
        server_id TEXT,
        user_id TEXT,
        warns INTEGER
    );
    '''
)

def setup_db(bot):
    with db_connection:
        db_cursor.executescript(create_statements)
        setup_users_and_servers(bot)
        bot.loop.create_task(clear_old_histories())

def get_user_warns(user_id, server_id):
    try:
        db_cursor.execute("SELECT warns FROM users WHERE user_id=? AND server_id=?", (user_id, server_id))
        result = db_cursor.fetchone()
        return result[0] if result else "" 
    except sqlite3.OperationalError:
        return ""  

def set_user_warns(user_id, server_id, warns_value):
    try:
        db_cursor.execute("UPDATE users SET warns=? WHERE user_id=? AND server_id=?", (warns_value, user_id, server_id))
        db_connection.commit()
    except sqlite3.OperationalError:
        pass  

def save_channel_config(server_id, channel_id, personality):
    with db_connection:
        db_cursor.execute(
            "INSERT OR REPLACE INTO channels (server_id, channel_id, personality) VALUES (?, ?, ?)",
            (server_id, channel_id, personality),
        )

def get_channel_history(channel_id):
    try:
        db_cursor.execute("SELECT history FROM channels WHERE channel_id=?", (channel_id,))
        result = db_cursor.fetchone()
        return result[0] if result and result[0] else ""
    except sqlite3.OperationalError as e:
        return ""

def save_channel_history(channel_id, new_message):
    retry_count = 3
    while retry_count > 0:
        try:
            with db_connection:
                db_cursor.execute(
                    "UPDATE channels SET history = ?, last_updated = CURRENT_TIMESTAMP WHERE channel_id = ?",
                    (new_message, channel_id),
                )
                if db_cursor.rowcount == 0:
                    pass
            return
        except sqlite3.OperationalError:
            retry_count -= 1
            time.sleep(1)

async def clear_old_histories():
    while True:
        await asyncio.sleep(60)
        with db_connection:
            db_cursor.execute(
                "UPDATE channels SET history = '' WHERE last_updated < datetime('now', '-10 minutes')"
            )
            db_connection.commit()

def update_channel_history(message, response):
    user_message = f"{message.author.name}: {message.content}"
    ai_response = f"AI: {response}"
    save_channel_history(message.channel.id, f"{get_channel_history(message.channel.id)}{user_message}\n{ai_response}")

def get_personality(message):
    db_cursor.execute(
        "SELECT personality FROM channels WHERE channel_id=?", 
        (message.channel.id,)
    )
    return db_cursor.fetchone()

def save_server(server_id):
    with db_connection:
        db_cursor.execute(
            "INSERT OR IGNORE INTO servers (server_id) VALUES (?)", (server_id,)
        )

def save_user(server_id, user_id):
    with db_connection:
        db_cursor.execute(
            "INSERT OR IGNORE INTO users (server_id, user_id) VALUES (?, ?)", (server_id, user_id)
        )

def setup_users_and_servers(bot):
    def server_exists(server_id):
        db_cursor.execute("SELECT 1 FROM servers WHERE server_id=?", (server_id,))
        return db_cursor.fetchone() is not None

    def user_exists(server_id, user_id):
        db_cursor.execute("SELECT 1 FROM users WHERE server_id=? AND user_id=?", (server_id, user_id))
        return db_cursor.fetchone() is not None

    async def check_for_new_servers_and_users():
        while True:
            for guild in bot.guilds:
                if not server_exists(guild.id):
                    save_server(guild.id)

                for member in guild.members:
                    if not user_exists(guild.id, member.id):
                        save_user(guild.id, member.id)
                        set_user_warns(member.id, guild.id, 0)

            await asyncio.sleep(30)

    bot.loop.create_task(check_for_new_servers_and_users())

    @bot.event
    async def on_guild_join(guild):
        if not server_exists(guild.id):
            save_server(guild.id)

        for member in guild.members:
            if not user_exists(guild.id, member.id):
                save_user(guild.id, member.id)
                set_user_warns(member.id, guild.id, 0)

    @bot.event
    async def on_member_join(member):
        if not user_exists(member.guild.id, member.id):
            save_user(member.guild.id, member.id)
            set_user_warns(member.id, member.guild.id, 0)

    @bot.event
    async def on_guild_remove(guild):
        try:
            db_cursor.execute("DELETE FROM users WHERE server_id=?", (guild.id,))
            db_connection.commit()
        
            db_cursor.execute("DELETE FROM servers WHERE server_id=?", (guild.id,))
            db_connection.commit()
        
            db_cursor.execute("DELETE FROM channels WHERE server_id=?", (guild.id,))
            db_connection.commit()
        except sqlite3.OperationalError:
            pass

    @bot.event
    async def on_channel_delete(channel):
        try:
            db_cursor.execute("DELETE FROM channels WHERE channel_id=?", (channel.id,))
            db_connection.commit()
        except sqlite3.OperationalError:
            pass

    @bot.event
    async def on_member_remove(member):
        try:
            db_cursor.execute("DELETE FROM users WHERE user_id=? AND server_id=?", (member.id, member.guild.id))
            db_connection.commit()
        except sqlite3.OperationalError:
            pass



import discord
from PIL import Image, ImageDraw
import random
import io
import requests
import colorsys
import typing

def setup(bot):
    @bot.tree.command(name="randomcolor", description="generate random color")
    async def randomcolor(interaction : discord.Interaction, color_code : typing.Literal['HSV', 'RGB', 'HEX']):
        if "RGB" in color_code:
            await RGB(interaction)
        elif "HSV" in color_code:
            await HSV(interaction)
        elif "HEX" in color_code:
            await HEX(interaction)
          
def generate_color_image(color):
    image = Image.new("RGB", (200, 200), color)
    return image

def upload_to_imgur(image_bytes, client_id):
    url = 'https://api.imgur.com/3/image'

    headers = {
        'Authorization': f'Client-ID {client_id}'
    }

    files = {'image': image_bytes.getvalue()}

    response = requests.post(url, headers=headers, files=files)
    imgur_url = response.json()['data']['link']

    return imgur_url

async def HSV(interaction):
          
    def hsv_to_rgb(h, s, v):
       r, g, b = colorsys.hsv_to_rgb(h / 360, s, v)
       return int(r * 255), int(g * 255), int(b * 255)
          
    hue = random.randint(0, 360)
    saturation = random.uniform(0.5, 1)
    value = random.uniform(0.5, 1)

    r, g, b = hsv_to_rgb(hue, saturation, value)
    color = r, g, b

    image = generate_color_image(color)
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    imgur_url = upload_to_imgur(image_bytes, 'bd876d2a4f8175e')

    embed = discord.Embed(
        title='Random Color HSV',
        description=f'HSV: {hue}, {saturation}, {value}',
        color=discord.Color.from_rgb(*color)
    )

    embed.set_image(url=imgur_url)
    await interaction.response.send_message(embed=embed)

async def HEX(interaction):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    color = r, g, b

    image = generate_color_image(color)
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    imgur_url = upload_to_imgur(image_bytes, 'bd876d2a4f8175e')

    embed = discord.Embed(
        title='Random Color HEX',
        description=(f'HEX: ' + hex_color),
        color=discord.Color.from_rgb(*color)
    )

    embed.set_image(url=imgur_url)
    await interaction.response.send_message(embed=embed)

async def RGB(interaction):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    image = generate_color_image(color)
    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    imgur_url = upload_to_imgur(image_bytes, 'bd876d2a4f8175e')

    embed = discord.Embed(
        title='Random Color RGB',
        description=f'RGB: {color[0]}, {color[1]}, {color[2]}',
        color=discord.Color.from_rgb(*color)
    )

    embed.set_image(url=imgur_url)
    await interaction.response.send_message(embed=embed)

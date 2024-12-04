import os
import importlib

def ai(bot):
    module = importlib.import_module("modules.AI.core")
    module.setup(bot)

def commands(bot):
    for root, dirs, files in os.walk("modules/commands"):
        for filename in files:
            if filename.endswith(".py"):
                module_name = f"{root.replace(os.sep, '.')}.{filename[:-3]}"
                module = importlib.import_module(module_name)
                module.setup(bot)

def instructions(file_path="instructions.txt"):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read()
    return "No instructions found."

def personalities(personalities_folder="modules/AI/personalities"):
    personalities = {}
    if os.path.exists(personalities_folder):
        for filename in os.listdir(personalities_folder):
            if filename.endswith(".txt"):
                with open(os.path.join(personalities_folder, filename), "r") as file:
                    personality_name = filename.replace(".txt", "")
                    personalities[personality_name] = file.read()
    return personalities
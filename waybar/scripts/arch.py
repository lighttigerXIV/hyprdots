#!/usr/bin/env python3

import os
import json
from os.path import expanduser

config_path = f"{expanduser("~")}/.config/waybar"

if os.path.exists(f"{config_path}/config.jsonc"):
    config_path = f"{config_path}/config.jsonc"
else:
    f"{config_path}/config"

with open(config_path, "r", encoding="utf-8") as file:
    config_json = json.loads(file.read())

module_configs = config_json["custom/arch"]
format = module_configs["format"]

print(format, flush=True)
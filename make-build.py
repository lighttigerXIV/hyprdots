import os
import subprocess
from os.path import expanduser

file_path = os.path.abspath(__file__)
file_dir = os.path.dirname(file_path)
home_dir = expanduser("~")
waybar_path = f""
mako_path = f"{home_dir}/.config/mako"

subprocess.run(f"rm -rf {file_dir}/waybar", shell=True)
subprocess.run(f"rm -rf {file_dir}/mako", shell=True)
subprocess.run(f"cp -r {home_dir}/.config/waybar {file_dir}", shell=True)
subprocess.run(f"cp -r {home_dir}/.config/mako {file_dir}", shell=True)

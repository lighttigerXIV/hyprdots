Dependencies
```sh
sudo pacman -S hyprland hyprpaper hyprlock hypridle xdg-desktop-portal-hyprland  gnome-keyring waybar pamixer mako brightnessctl wl-clipboard
```

Aur Dependencies
```
yay hyprshade
```

Config hyprshade
```
hyprshade install
systemctl --user enable --now hyprshade.timer
```
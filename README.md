# fcitx-skin-material
A Material Design-like skin for Fcitx.

# インストール
`material` フォルダを `~/.config/fcitx/skin` にコピーしてください。  
Arch Linuxを使っている場合、[AURパッケージ](https://aur.archlinux.org/packages/fcitx-skin-material/)でもインストールできます。

# Installation
## Fcitx 4:
Copy `material` to `~/.config/fcitx/skin`.

## Fcitx 5:
Copy `material` to `~/.local/share/fcitx5/themes`. Quit fcitx5 if it's
running, then create `~/.config/fcitx5/conf/classicui.conf` with following
content:

```
Theme=material
# depends on your preference
Vertical Candidate List=True
Font="Sans Serif 12"
```

For Arch users:
- [Arch Linux Chinese Community Repository](https://github.com/archlinuxcn/repo)
- [AUR package](https://aur.archlinux.org/packages/fcitx-skin-material/)

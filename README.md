# fcitx-skin-material
A Material Design-like skin for Fcitx.

# インストール
## Fcitx 4
`material` フォルダを `~/.config/fcitx/skin` にコピーします。  
Arch Linuxを使っている場合、[AURパッケージ](https://aur.archlinux.org/packages/fcitx-skin-material/)でもインストールできます。

## Fcitx 5
`material` フォルダを `~/.local/share/fcitx5/themes` にコピーして、 `~/.config/fcitx5/conf/classicui.conf` を以下の内容で作成します。

```
Theme=material
# 以下は必要に応じて変更
Vertical Candidate List=True
Font="Sans Serif 12"
```

# Installation
## Fcitx 4
Copy `material` to `~/.config/fcitx/skin`.

For Arch users:
- [Arch Linux Chinese Community Repository](https://github.com/archlinuxcn/repo)
- [AUR package](https://aur.archlinux.org/packages/fcitx-skin-material/)

## Fcitx 5
Copy `material` to `~/.local/share/fcitx5/themes`. Quit fcitx5 if it's
running, then create `~/.config/fcitx5/conf/classicui.conf` with following
content:

```
Theme=material
# depends on your preference
Vertical Candidate List=True
Font="Sans Serif 12"
```

#!/bin/bash

echo "=========== Install ZeroNet Browser for Linux ==========="
cat > .desktop << EOF
[Desktop Entry]
Version=0.1
Name=ZeroNet Browser
Comment=ZeroNet browser is a dedicated browser for ZeroNet protocol.
Exec=$HOME/.local/share/ZeronetBrowser/ZeronetBrowser
Path=$HOME/.local/share/ZeronetBrowser/
Icon=$HOME/.local/share/ZeronetBrowser/icons/zeronet-logo.svg
Terminal=true
Type=Application
Categories=Utility;
EOF

cp ./.desktop ~/.local/share/applications/zeronet-browser.desktop
chmod +x ~/.local/share/applications/zeronet-browser.desktop
mkdir ~/.local/share/ZeronetBrowser
cp -a . ~/.local/share/ZeronetBrowser
cd ~/.local/share/ZeronetBrowser
ln -s $PWD/ZeronetBrowser $HOME/.local/bin/ZeronetBrowser
echo "Done !"

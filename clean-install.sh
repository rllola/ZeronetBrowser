#!/bin/bash

echo "=========== Uninstall ZeroNet Browser for Linux ==========="

rm ~/.local/share/applications/zeronet-browser.desktop
rm -rf ~/.local/share/ZeronetBrowser
rm $HOME/.local/bin/ZeronetBrowser
echo "Done !"

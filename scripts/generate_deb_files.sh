#!/bin/bash

echo "====== GENERATE CONTROL FILE ======"
cat > $PWD/pkg-debian/DEBIAN/control << EOF
Package: ZeronetBrowser
Version: ${TRAVIS_TAG/v}
Architecture: all
Essential: no
Section: web
Priority: optional
Maintainer: Lola Rigaut-Luczak
Description: Browser for Zeronet.
EOF

mkdir -p $PWD/pkg-debian/usr/share/applications/

echo "====== GENERATE .DESKTOP FILE ======"
cat > $PWD/pkg-debian/usr/share/applications/zeronet-browser.desktop << EOF
[Desktop Entry]
Version=${TRAVIS_TAG/v}
Name=ZeroNet Browser
Comment=ZeroNet browser is a dedicated browser for ZeroNet protocol.
Exec=ZeronetBrowser %u
Path=/usr/share/ZeronetBrowser/
Icon=/usr/share/ZeronetBrowser/icons/zeronet-logo.svg
Terminal=true
Type=Application
Categories=Application;Network;
MimeType=x-scheme-handler/zero;
EOF

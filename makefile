# Build a .deb package for test
build:
	pyinstaller browser.spec
	mv dist/ZeronetBrowser pkg-debian/usr/share/
	dpkg -b pkg-debian ZeronetBrowser_test_amd64.deb

clean:
	rm -rf dist/ build/
	rm -rf pkg-debian/usr/share/ZeronetBrowser
	rm *.deb

.PHONY: build clean

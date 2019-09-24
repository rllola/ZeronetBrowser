# Build a .deb package for test
build:
	pyinstaller browser.spec
	mv dist/ZeronetBrowser pkg-debian/usr/share/
	dpkg -b pkg-debian ZeronetBrowser_test_i386.deb

clean:
	rm -rf dist/ build/
	rm -rf pkg-debian/usr/share/ZeronetBrowser
	rm *.deb

tag:
	./scripts/bump_version.sh
	git tag ${TAG}


.PHONY: build clean

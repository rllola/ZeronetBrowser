import sys, os

version = '0.0.0'

if 'TRAVIS_TAG' in os.environ:
    version = os.environ['TRAVIS_TAG'][1:]
elif 'APPVEYOR_REPO_TAG_NAME' in os.environ:
    version = os.environ['APPVEYOR_REPO_TAG_NAME'][1:]
else:
    sys.exit()

file = open("src/version.py", "w")

file.write("VERSION = '{}'".format(version))

file.close()

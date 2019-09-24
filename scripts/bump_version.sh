#!/bin/bash

echo "====== BUMP VERSION ${TRAVIS_TAG} ======"
cat > $PWD/src/version.py << EOF
VERSION = '${TRAVIS_TAG/v}'
EOF

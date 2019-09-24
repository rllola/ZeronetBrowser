#!/bin/bash

echo "====== BUMP VERSION ${TAG} ======"
cat > $PWD/src/version.py << EOF
VERSION = '${TAG/v}'
EOF

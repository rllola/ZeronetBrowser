#!/bin/bash

for f in ./*.so.*; do
  echo $f
  LD_LIBRARY_PATH=. ldd $f | grep 'not found'
done

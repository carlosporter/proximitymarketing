#!/bin/bash

CWD=$(pwd)
source prepare_installer.sh

VERSION=$(cat $CWD/latest-version)
cd $OP2
mv openproximity2 openproximity2-$VERSION

echo "creating official release $VERSION" 

tar --numeric-owner -h --group=0 --exclude=\*svn --owner=0 -czf $CWD/openproximity2-$VERSION.tar.gz openproximity2-$VERSION

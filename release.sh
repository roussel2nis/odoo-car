#!/bin/sh
VERSION=`cat VERSION.txt`
read -p "Tag and release version $VERSION? [yN] " yn
if [ "$yn" = "y" ] ; then
    # tag addons-deldrive
    cd car-addons
    git diff --exit-code || { echo "Please commit first!" ; exit 1 ; }
    git tag -a tag_release$VERSION -m 'tag version '$VERSION
    git push --tag
    cd ..
    # tag buildout
    git diff --exit-code || { echo "Please commit first!" ; exit 1 ; }
    git tag -a tag_release$VERSION -m 'tag version '$VERSION
    git push --tag
    # release
fi
bin/buildout install odoo_release

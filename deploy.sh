#!/bin/bash
# If the 'release' directory on the target
# machine is owned by a different user than
# the user deploying (which is probably the case),
# it must be writeable by the 'odoodeploy'
# group, and the remote user for rsync must
# be part of the 'odoodeploy' group.
# The permissions on the 'release' directory 
# must be drwxrwsr-x (the setgid is important).
if [ $# -lt 2 ]
then
        echo "Usage : $0 remote_user instance"
        exit
fi

case $2 in
  "prod1")
    TARGET=""
    INSTANCE="prod"
  ;;
  "recette")
    TARGET="149.202.173.63"
    INSTANCE="test"
  ;;
  *) echo "$2 unknow instance"
esac

if [ -z $1 ] || [ -z $INSTANCE ]
then
  echo "user or instance not correctly set"
else
  rsync \
  --verbose \
  --recursive \
  --times \
  --links \
  --delete \
  --omit-dir-times \
  release/ \
    $1@$TARGET:/home/odoo-$INSTANCE/instance/release/
fi

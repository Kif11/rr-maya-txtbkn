#!/usr/bin/env bash

CURDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export PYTHONPATH=$CURDIR

export MAYA_MODULE_PATH=$CURDIR
export MAYA_PROJECT=$CURDIR/test/simple_cube

echo "--------------------------------------------------------------------------"
echo "PYTHONPATH: $PYTHONPATH"
echo "MAYA_MODULE_PATH: $MAYA_MODULE_PATH"
echo "MAYA_PROJECT: $MAYA_PROJECT"
echo "--------------------------------------------------------------------------"

COMMAND="$1"

if [ "$COMMAND" = "run" ]
then
    python ./app.py

elif [ "$COMMAND" = "test" ]
then
    python ./tests/simple_test.py
elif [ "$COMMAND" = "maya" ]
then
    /Applications/Autodesk/maya2015/Maya.app/Contents/bin/maya -file $CURDIR/tests/simple_cube/scenes/cube_and_plane_v001.ma
elif [ "$COMMAND" = "mayacmd" ]
then
    /Applications/Autodesk/maya2015/Maya.app/Contents/bin/mayapy -i startup.py
    #-file $CURDIR/tests/simple_cube/scenes/cube_and_plane_v001.ma
else
    echo "Command is unknown"
fi

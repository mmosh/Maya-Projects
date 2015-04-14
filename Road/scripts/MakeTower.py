#RandomRectangles.py
import maya.cmds as cmds
import random

random.seed( 12 )
'''
few lines of comment
are written
in this section
'''
'''cubeList = cmds.ls( 'theCube*')
if len(cubeList) >0:
    cmds.delete( cubeList )
result = cmds.polyCube ( w = 1, h= 1, d = 1, name= 'theCube#')
'''
result = cmds.ls (orderedSelection = True)

print 'result: %s' % (result)


if len (result) >= 2:
    floor = result[0]
    windows = result[1]
    floorGroup = cmds.group(empty = True, name= floor + '_floor_grp#')
    windowGroup = cmds.group(empty = True, name= floor + '_window_grp#')
    for i in range (0, 8):
        floorInstance = cmds.instance( floor, name=floor + '_instance#')
        cmds.parent (floorInstance, floorGroup)
        x = 0
        y = (i*30) + 15
        z = -900
        cmds.move(x, y, z, floorInstance )
        
        floorScale = cmds.xform( q=True, s=True)
        #print 'floorX: %s' % (floorScale[0])
        if i<7:
            windowInstance = cmds.instance(windows, name=windows+'_instance#')
            cmds.parent (windowInstance, windowGroup)
            x = -52#-floorScale[0]/2
            y = (i*30) -60#+ 30
            z = -32#-900
            cmds.move(x, y, z, windowInstance )
            windowInstance = cmds.instance(windows, name=windows+'_instance#')
            cmds.parent (windowInstance, windowGroup)
            x = 102#floorScale[0]/2
            y = (i*30) -60#+ 30
            z = -32#-900
            cmds.move(x, y, z, windowInstance )
            windowInstance = cmds.instance(windows, name=windows+'_instance#')
            cmds.parent (windowInstance, windowGroup)
            x = 25
            y = (i*30) -60#+ 30
            z = -112#-900+floorScale[2]/2
            cmds.move(x, y, z, windowInstance )
            yRot = 90
            zRot = 180
            cmds.rotate(0,yRot,zRot,windowInstance)
            windowInstance = cmds.instance(windows, name=windows+'_instance#')
            cmds.parent (windowInstance, windowGroup)
            x = 25#random.uniform(0, 10)
            y = (i*30) -60#+ 30#random.uniform(0, 10)
            z = 52#-900-floorScale[2]/2#random.uniform(0, 10)
            cmds.move(x, y, z, windowInstance )
            yRot = 90
            zRot = 180
            cmds.rotate(0,yRot,zRot,windowInstance)
        
        #cmds.hide (transformName)
        #cmds.delete(transformName)

    cmds.xform(floorGroup, centerPivots=True )
    
else:
    print 'Please select a floor followed by a window'


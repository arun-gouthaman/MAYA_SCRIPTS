import pymel.all as pm
import maya.OpenMaya as OpenMaya
if pm.commandPort(':7720', q=True) !=1:
   pm.commandPort(n=':7720', eo = False, nr = False)
   OpenMaya.MGlobal.displayInfo("Port opened-----7720")
else:
   OpenMaya.MGlobal.displayInfo("Port already open-----7720") 
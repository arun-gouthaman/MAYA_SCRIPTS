import pymel.all as pm
import maya.OpenMaya as OpenMaya
# Assign orientation of first selected joint to the rest

def copy_orientation():
    sel = pm.ls(selection=True)
    prnt = sel.pop(0)
    for obj in sel:
        tmp_con = pm.orientConstraint(prnt, obj, maintainOffset=False, name="tmp")
        pm.delete(tmp_con)
        pm.makeIdentity(apply=True, translate=True, rotate=True, scale=True, normal=False, preserveNormals =True)
    return None


#Insert joint/s between 2 joints
def ins_jnt(**kwargs):
    num = kwargs.get("num_jts", 1)
    sel = pm.ls(selection=True)
    chld = pm.listRelatives(sel[0], children=True)
    if not chld[0].type() == "joint":
        print "end joint reached"
        return None
    #position_lst = []
    pos1 = pm.xform(sel[0], query=True, worldSpace=True, translation=True)
    pos2 = pm.xform(chld, query=True, worldSpace=True, translation=True)
    len_vec1 = OpenMaya.MVector(pos1[0],pos1[1],pos1[2])
    len_vec2 = OpenMaya.MVector(pos2[0],pos2[1],pos2[2])
    len_vec = len_vec2-len_vec1
    print len_vec.x, len_vec.y, len_vec.z
    part_vec = len_vec/(num+1)
    pos_vec = len_vec1+len_vec/(num+1)
    cur_jnt = sel[0]
    for i in range(num):
        new_position = [pos_vec.x, pos_vec.y, pos_vec.z]
        #print new_position
        new_joint = pm.insertJoint(cur_jnt)
        pm.joint(new_joint, edit=True, component = True, position = new_position)
        #pm.xform(new_joint, translation=new_position)
        pos_vec += part_vec
        cur_jnt = new_joint
    return None

def curve_through_points(**kwargs):
    selection_points = pm.ls(selection=True)
    mt_pth = kwargs.get("motion_path", False)
    if len(selection_points)<2:
        print "please select more than one points"
        return None
    curve_name = kwargs.get("curve_name", "")
    curve_degree = kwargs.get("curve_degree", 1)
    points_locations = []
    for point in selection_points:
        points_locations.append(pm.xform(point, query=True, translation=True, worldSpace=True))
    pm.select(clear=True)
    current_curve = pm.curve(degree = curve_degree, worldSpace=True, point = points_locations)
    pm.rename(current_curve, curve_name)
    print "CRV", current_curve
    if mt_pth:
        motion_path(objs = selection_points, path_curve = current_curve)
    return None
#curve_through_points(curve_name = "curve", curve_degree = 3)


def motion_path(**kwargs):
    objs =  kwargs.get("objs", None)
    point = int(len(objs)/2)
    print objs[point]
    loc = pm.spaceLocator(name="up_loc")
    tmp_con = pm.parentConstraint(objs[point], loc, maintainOffset=False)
    pm.delete(tmp_con)
    pm.move(loc, 10, moveY=True, objectSpace=True)
    parts = 1.0/float((len(objs)-1))
    crv = kwargs.get("path_curve", None)
    print objs
    #print crv
    initU = 0.0
    pm.select(clear=True)
    #for obj in objs:
        #path_anim = pm.pathAnimation(obj, curve = crv, follow=True, followAxis = "x", upAxis = "y", 
        #                             worldUpType = "object", worldUpObject = loc, fractionMode=True)
        #path_anim = pm.pathAnimation(obj, curve = crv, follow=True, followAxis = "x", upAxis = "y", 
        #                             worldUpType = "vector", worldUpVector = [0,1,0], fractionMode=True)
        #pm.disconnectAttr(str(path_anim)+".uValue")
        #pm.setAttr(str(path_anim)+".uValue", initU)
        #initU += float(parts)
    return None


def center_position2(**kwargs):
    selected_items = kwargs.get("selected_items", [])
    #selected_items = pm.ls(selection=True, flatten=True)
    number_of_items = len(selected_items)
    print number_of_items
    position_vector = []
    final_vector = OpenMaya.MVector(0,0,0)
    for index in range(number_of_items):
        pos = pm.xform(selected_items[index], query=True, worldSpace=True, translation=True)
        vec = OpenMaya.MVector(pos[0], pos[1], pos[2])
        position_vector.append(vec)
    
    for vector_index in range(len(position_vector)):
        final_vector = final_vector + position_vector[vector_index]
    
    final_vector = final_vector/len(position_vector)
    mid_position = [final_vector.x, final_vector.y, final_vector.z]
    return mid_position



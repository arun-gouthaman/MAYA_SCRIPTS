import pymel.all as pm
import maya.mel as mel
#gMainWindowStr = pm.mel.eval ('global string $gMainWindow; string $temp=$gMainWindow;')
pm.selectPref(trackSelectionOrder=True)
def obj_creat():
    import object_creator_ui
    object_creator_ui.object_creator_ui()
    return None
    
def cus_tls():
    import CustomScriptsUI
    CustomScriptsUI.CustomScripts_UI()
    return None

def con_tls():
    import constraintsUI
    constraintsUI.constraints_ui()   
    return None


def tank_trd():
    import TreadCreateUI
    TreadCreateUI.tankTread_UI()
    return None

def copy_sdk():
    import copySDKUI
    copySDKUI.copySDK_UI()    
    return None

def cus_tls():
    import CustomScriptsUI
    CustomScriptsUI.CustomScripts_UI()
    return None

def api_doc():
    import ToolScripts
    ToolScripts.open_api_doc()
    return None

def def_to_sk_cl():
    import All_Deformers_2_SkinCluster
    All_Deformers_2_SkinCluster.All_Deformer_2_SkinCluster() 
    return None

def skin_xfer():
    mel.eval('source "skinXfer-v1.5-";')
    mel.eval('skinXfer;')
    return None    

def mir_cls():
    import sl_mirroCluster
    sl_mirroCluster.sl_mirroClusterUI()
    return None    

    
def qa_sk_mng():
    mel.eval('source "qa_skinManagerUI";')
    mel.eval('qa_skinManagerUI;')
    return None    

   
def stretch_setup():
    mel.eval('source "MyjsScaleJointsByCurve_final";')
    mel.eval('jsScaleJointsByCurve;')
    return None

def jnt_along_loop():
    import Jntpos
    Jntpos.jnt_along_loop()
    return None

def jnt_at_mid():
    import Jntpos
    Jntpos.jnt_at_object_mid()
    return None

def jnt_mid_aimed():
    import Jntpos
    Jntpos.jnt_at_mid_vertex_orient()
    return None

def spline_ik_setup():
    import Ik_Spline_Setup_Ui
    Ik_Spline_Setup_Ui.spline_ik_setup_UI()
    return None

def curve_points():
    import CustomScripts
    CustomScripts.curve_through_points()
    return None

def insert_joints():
    import insertJointsUI
    insertJointsUI.insert_joints_UI()
    return None    
    
menuName = "Custom_Menu"
mainMenu = pm.PyUI( pm.getMelGlobal('string', 'gMainWindow') )

try:
    if pm.menu(Custom_Tools, query=True, exists=True):
        pm.deleteUI(Custom_Tools)
except:
    print "Creating New Menu"

with mainMenu:
    if pm.menu(menuName, query=True, exists = True):
        pm.menu(menuName, edit=True, deleteAllItems=True)
    #Custom_Tools = pm.menu( label=menuName, tearOff=True )
    Custom_Tools = pm.menu(label=menuName)
    with Custom_Tools:
        obj_cr_btn = pm.menuItem( label="Object creator",command=lambda x: obj_creat())
        cus_tls_btn = pm.menuItem( label="Custom Tools",command=lambda x: cus_tls())
        const_btn = pm.menuItem( label="Constraint",command=lambda x: con_tls())
        tnk_trd_bth = pm.menuItem( label="Tank Tread Rig (arun)", command=lambda x: tank_trd())
        cpy_sdk_btn = pm.menuItem( label="Copy Sdk (arun)", command=lambda x: copy_sdk())
        #tools_btn = pm.menuItem(subMenu=True, label = "Tools", tearOff=True)
        #tool_sub1_btn = pm.menuItem(label = "Test")
        joint_place_btn = pm.menuItem(subMenu=True, label = "Joint Placement", tearOff=True)
        joint_place_sub1_btn = pm.menuItem(label = "Center", command = lambda x: jnt_at_mid())
        joint_place_sub2_btn = pm.menuItem(label = "Center aimed at vertex", command = lambda x: jnt_mid_aimed())
        joint_place_sub3_btn = pm.menuItem(label = "Chain along edge loops", command = lambda x: jnt_along_loop())
        
        
        pm.setParent('..', menu=True)
        skn_clstr_btn = pm.menuItem(subMenu=True, label = "Skin Cluster Tools")
        tool_sub_def_skn = pm.menuItem(label = "All deformers to skin cluster (suresh)", command = lambda x: def_to_sk_cl())
        tool_sub_xfer = pm.menuItem(label = "SkinXfer (suresh)", command = lambda x: skin_xfer())
        tool_sub_qaSknMng = pm.menuItem(label = "qa skin manager (amit das)", command = lambda x: qa_sk_mng())
        
        pm.setParent('..', menu=True)
        clst_tl_btn = pm.menuItem(subMenu=True, label = "Cluster tools")
        cls_sub_mir = pm.menuItem(label = "Mirror Cluster (amit das)", command = lambda x: mir_cls())
        
        pm.setParent('..', menu=True)
        scl_jnts_crv = pm.menuItem( label="Scale Joints By Curve (amit das)", command=lambda x: stretch_setup())
        
        spline_ik = pm.menuItem( label="IK spline setup (arun)", command=lambda x: spline_ik_setup())
        
        curve_through_points = pm.menuItem(label = "curve through points", command = lambda x: curve_points())
        
        insert_Joints = pm.menuItem(label = "insert joints", command = lambda x: insert_joints())
        
        api_doc_btn = pm.menuItem(label = "API DOC", command=lambda x: api_doc())
        
        
pass
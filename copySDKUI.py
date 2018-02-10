import pymel.all as pm
import copy_SDK
#reload (copy_SDK)
def populate_attr(**kwargs):
    scroll_lst = kwargs.get("field_obj", None)
    sel_src = pm.ls(selection=True)
    if not sel_src:
        print "no object selected"
        return None
    scroll_lst.removeAll()
    for attr in pm.listAttr(sel_src[0], keyable=True):
        scroll_lst.append(str(attr))
    return None

def sdk_call(mode_obj, attributes_obj, search_obj, replace_obj, mirror_obj, att_chk):
    sel_mode = mode_obj.getSelect()
    mode_opn = str(pm.radioButton(sel_mode, query=True, label = True))
    srch_txt = search_obj.getText()
    rplc_txt = replace_obj.getText()
    attrs_sel = pm.textScrollList(attributes_obj, query=True, selectItem=True)
    mirror_val = pm.checkBox(mirror_obj, query=True, value=True)
    att_val = False
    if str(mode_opn) == "driver":
        att_val = pm.checkBox(att_chk, query=True, value=True)
    if not mirror_val:
        if srch_txt=="" or rplc_txt=="":
            copy_SDK.copySDK(curAttrs = attrs_sel, mode = mode_opn, 
                             createDriverAttr = att_val)
        else:
            copy_SDK.copySDK(curAttrs = attrs_sel, mode = mode_opn, search = srch_txt,
                    replace = rplc_txt, createDriverAttr = att_val)
    else:
        if srch_txt=="" or rplc_txt=="":
            copy_SDK.copySDK(curAttrs = attrs_sel, mode = mode_opn, 
                    mirrorAttrs = attrs_sel, createDriverAttr = att_val)
        else:
            copy_SDK.copySDK(curAttrs = attrs_sel, mode = mode_opn, search = srch_txt,
                    mirrorAttrs = attrs_sel, replace = rplc_txt, createDriverAttr = att_val)
    return None


def copySDK_UI():
    WINDOW='copySDK'
    if pm.window(WINDOW, query=True, exists=True):
        pm.deleteUI(WINDOW)
    pm.window(WINDOW, title="copySDK", iconName='SDKcpy', 
              widthHeight=(210, 370) )
    
    # Layout
    column_1=pm.columnLayout( adjustableColumn=True )
    textlabel = pm.text(label = "UI for script downloaded from\
                                 highend3d.com\nContact Email : martinik24@gmail.com",
                                 align = "center", wordWrap=True)
    pm.separator( height=20, style='in', parent=column_1 )
    col2 = pm.columnLayout(width = 200, adjustableColumn = False, parent=column_1)
    row_col_1 = pm.rowColumnLayout(numberOfColumns = 2, columnWidth = (1, 100), 
                parent = column_1, columnOffset = (2, 'left', 10))
    pm.separator( height=20, style='in', parent=column_1 )    
    col3 = pm.columnLayout(width = 200, adjustableColumn = False, parent=column_1)
    row_col_2 = pm.rowColumnLayout(numberOfColumns = 2, columnWidth = (1, 100), 
                                   parent = column_1, columnOffset = (2, 'left', 10))
    row_col_3 = pm.rowColumnLayout(numberOfColumns = 2, columnWidth = (1, 100), 
                                   parent = column_1, columnOffset = (2, 'left', 10))
    pm.separator( height=20, style='in', parent=column_1 )
    row_col_4 = pm.rowColumnLayout(numberOfColumns = 2, columnWidth = (1, 100), 
                                   parent = column_1, columnOffset = (2, 'left', 10))
    row_col_5 = pm.rowColumnLayout(numberOfRows = 2, parent = row_col_4)
    column_2=pm.columnLayout( adjustableColumn=False, width = 200, 
                              columnOffset=["both",50], parent = column_1)

    
    # Widgets
    cr_attr_chk_bx = pm.checkBox('Create attribute', parent = column_2, editable=False)
    mode_lbl = pm.text(label = "mode", align = "center", parent = col2, width=200)
    mode_radio = pm.radioCollection(parent = column_1)
    rb1 = pm.radioButton( label='driven', parent = row_col_1, select=True, onCommand = lambda x:pm.checkBox(cr_attr_chk_bx, edit=True, editable=False))
    rb1 = pm.radioButton( label='driver', parent = row_col_1, select=False, onCommand = lambda x:pm.checkBox(cr_attr_chk_bx, edit=True, editable=True))
    
    ctr_replace_lbl = pm.text(label = "controller", align = "center", 
                              parent = col3, width=200)
    search_lbl = pm.text(label = "search", align = "center", 
                              parent = row_col_2, width=100)
    replace_lbl = pm.text(label = "replace", align = "center", 
                              parent = row_col_2, width=100)
    search_str=pm.TextField(text='', parent = row_col_3)
    replace_str=pm.TextField(text='', parent = row_col_3)
    refresh_button = pm.button(label='Refresh', parent = row_col_5,
                               command = lambda x: populate_attr(field_obj = attr_list))
    attr_list=pm.textScrollList('Attr', numberOfRows=10, parent = row_col_5, 
                                 height=150, width = 100, allowMultiSelection=True)
    populate_attr(field_obj = attr_list)
    mirror_chk_bx = pm.checkBox('mirror', parent = row_col_4)
    
    apply_button = pm.button(label='Apply', parent = column_2, width = 100,
                             command=lambda x: sdk_call(mode_radio, attr_list, 
                              search_str, replace_str, mirror_chk_bx, 
                              cr_attr_chk_bx))
    
    pm.showWindow(WINDOW)
    pm.window(WINDOW, edit=True, widthHeight=(210, 370))
    return None
copySDK_UI()
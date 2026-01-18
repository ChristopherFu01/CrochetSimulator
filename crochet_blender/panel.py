import bpy

class CROCHET_PT_panel(bpy.types.Panel):
    bl_label = "CrochetPARADE"
    bl_idname = "CROCHET_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Crochet'

    def draw(self, context):
        layout = self.layout
        layout.operator("crochet.generate")
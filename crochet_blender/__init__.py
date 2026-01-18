bl_info = {
    "name": "CrochetPARADE (Python)",
    "blender": (3, 0, 0),
    "category": "Object"
}

from .operators import CROCHET_OT_generate
from .panel import CROCHET_PT_panel

def register():
    import bpy
    bpy.utils.register_class(CROCHET_OT_generate)
    bpy.utils.register_class(CROCHET_PT_panel)

def unregister():
    import bpy
    bpy.utils.unregister_class(CROCHET_OT_generate)
    bpy.utils.unregister_class(CROCHET_PT_panel)
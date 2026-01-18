import bpy # blender
from .parser import parse_pattern
from .geometry import layout_stitches, create_stitch_mesh

class CROCHET_OT_generate(bpy.types.Operator):
    bl_idname = "crochet.generate"
    bl_label = "Generate Crochet Pattern"

    pattern: bpy.props.StringProperty(
        name="Pattern",
        default="ch, 5*sc, dc"
    )

    def execute(self, context):
        pattern = parse_pattern(self.pattern)
        stitches = layout_stitches(pattern)

        for s in stitches:
            create_stitch_mesh(
                f"stitch_{s['id']}_{s['kind']}",
                s["position"]
            )

        return {'FINISHED'}
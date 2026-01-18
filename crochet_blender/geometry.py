import bpy
import mathutils

STITCH_RADIUS = 0.03
STITCH_HEIGHT = 0.1

# geometry builder (mesh per stitch)
def create_stitch_mesh(name, location):
    bpy.ops.mesh.primitive_cylinder_add(
        radius=STITCH_RADIUS,
        depth=STITCH_HEIGHT,
        location=location
    )
    obj = bpy.context.object
    obj.name = name
    return obj

# layout algorithm (row construction)
def layout_stitches(pattern):
    stitches = []
    pos = mathutils.Vector((0, 0, 0))
    direction = mathutils.Vector((1, 0, 0))

    for i, stitch_type in enumerate(pattern):
        stitch = {
            "id": i,
            "kind": stitch_type,
            "position": pos.copy()
        }
        stitches.append(stitch)

        pos += direction * STITCH_HEIGHT

        if stitch_type == "ch":
            direction.rotate(
                mathutils.Euler((0, 0, 0.1))
            )

    return stitches
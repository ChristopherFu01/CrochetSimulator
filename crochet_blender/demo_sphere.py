import bpy
import mathutils

# -----------------------------
# Clean scene
# -----------------------------
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# -----------------------------
# Pattern parser
# -----------------------------
def parse_pattern(text):
    tokens = [t.strip() for t in text.split(",")]
    pattern = []

    for tok in tokens:
        if "*" in tok:
            n, stitch = tok.split("*")
            pattern.extend([stitch] * int(n))
        else:
            pattern.append(tok)

    return pattern

# -----------------------------
# Layout logic
# -----------------------------
STITCH_SPACING = 0.15
TURN_ANGLE = 0.15

def layout_stitches(pattern):
    stitches = []

    pos = mathutils.Vector((0, 0, 0))
    direction = mathutils.Vector((1, 0, 0))

    for i, kind in enumerate(pattern):
        stitches.append({
            "id": i,
            "kind": kind,
            "position": pos.copy()
        })

        # Move forward
        pos += direction * STITCH_SPACING

        # Chains slightly curve
        if kind == "ch":
            direction.rotate(
                mathutils.Euler((0, 0, TURN_ANGLE))
            )

    return stitches

# -----------------------------
# Geometry creation (SPHERES)
# -----------------------------
def create_stitch_sphere(stitch):
    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=0.04,
        location=stitch["position"]
    )
    obj = bpy.context.object
    obj.name = f"stitch_{stitch['id']}_{stitch['kind']}"

    # Color by stitch type
    mat = bpy.data.materials.new(name=f"mat_{stitch['kind']}")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]

    if stitch["kind"] == "ch":
        bsdf.inputs["Base Color"].default_value = (0.9, 0.8, 0.2, 1)
    elif stitch["kind"] == "sc":
        bsdf.inputs["Base Color"].default_value = (0.2, 0.7, 0.9, 1)
    elif stitch["kind"] == "dc":
        bsdf.inputs["Base Color"].default_value = (0.9, 0.4, 0.4, 1)
    else:
        bsdf.inputs["Base Color"].default_value = (0.8, 0.8, 0.8, 1)

    obj.data.materials.append(mat)
    return obj

# -----------------------------
# DEMO EXECUTION
# -----------------------------
pattern_text = "ch, ch, ch, 5*sc, dc, dc, ch, 3*sc"

pattern = parse_pattern(pattern_text)
stitches = layout_stitches(pattern)

for stitch in stitches:
    create_stitch_sphere(stitch)

# Add camera
bpy.ops.object.camera_add(
    location=(0, -3, 1.5),
    rotation=(1.2, 0, 0)
)

# Add light
bpy.ops.object.light_add(
    type='AREA',
    location=(0, -2, 2)
)

print("CrochetPARADE sphere demo complete.")
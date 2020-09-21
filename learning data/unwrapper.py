import bpy
import bmesh

from math import radians

context = bpy.context
scene = context.scene

# Create a sphere

# Create an empty mesh and the object.
mesh = bpy.data.meshes.new('Basic_Sphere')
basic_sphere = bpy.data.objects.new("Basic_Sphere", mesh)

# Add the object into the scene.
bpy.context.collection.objects.link(basic_sphere)

# Select the newly created object
bpy.context.view_layer.objects.active = basic_sphere
basic_sphere.select_set(True)

# Construct the bmesh sphere and assign it to the blender mesh.
bm = bmesh.new()
bmesh.ops.create_uvsphere(bm, u_segments=32, v_segments=16, diameter=1)
for f in bm.faces:
    f.select_set(True)


# Unwrap all objects

for obj in scene.objects:
    if (obj.type == 'MESH'):

        context.view_layer.objects.active = obj
        obj.select_set(True)
        print(obj.name)
        lm =  obj.data.uv_layers.get("LightMap")
        if not lm:
            lm = obj.data.uv_layers.new(name="LightMap")
        lm.active = True
        bpy.ops.object.editmode_toggle()
        bpy.ops.uv.smart_project()
        bpy.ops.object.editmode_toggle()
        obj.select_set(False)
import bpy
import os


def ls(cdir):  # return directory contents of cdir
    ls = os.listdir(cdir)
    return ls


sc = bpy.data.scenes[0]  # get current scene
imgdir = "C:\\images"
img_ext = 'jpg'

files = []  # list for files
images = []  # list for imgage files
files = (ls(imgdir))  # read file list into list
file_count = len(files)  # file count

for a in range(0, file_count):  # for each file:
    if files[a].endswith(img_ext):  # does it end with?
        images.append(files[a])  # if so then add to images list

image_count = len(images)  # count of images
print(file_count)
print(image_count)

for a in range(0, image_count):  # for each image
    print("========================")
    print('loop count: ' + str(a))
    bpy.ops.mesh.primitive_plane_add()
    plane = bpy.context.scene.objects.active

    mat = bpy.data.materials.new('mat' + str(a))
    bpy.context.object.data.materials.append(mat)

    tex = bpy.data.textures.new('ColorTex', type='IMAGE')
    imgpath = imgdir + '\\' + images[a]  # make string with path ti image
    img = bpy.data.images.load(imgpath)  # load image
    tex.image = img
    mtex = mat.texture_slots.add()
    mtex.texture = tex

    imgX = img.size[0] / 1000.0  # calculate dimensions
    imgY = img.size[1] / 1000.0

    plane.scale[0] = (imgX)  # set x plane dimensions to match image
    plane.scale[1] = (imgY)  # set y plane dimensions to match image

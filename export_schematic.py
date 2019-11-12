'''this is a comment
'''

def save_schematic(context, filepath):
    scene = context.scene
    obj = context.active_object
    
    filehandle = open(filepath, 'w')
    fw = filehandle.write
    
    fw("Hello World")
    
    filehandle.close()
    return {'FINISHED'}

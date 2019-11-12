bl_info = {
    "name": "Export as .schematic",
    "author": "Me",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "File > Import/Export > Schematic (.schematic)",
    "description": "Import/Export schematics from minecraft",
    "warning": "",
    "wiki_url": "",
    "category": "Import-Export",
}

if "bpy" in locals():
    import importlib
    if "export_schematic" in locals():
        importlib.reload(export_schematic)

import bpy
from bpy.types import Operator
from bpy_extras.io_utils import ExportHelper
from bpy.props import (
        StringProperty,
        BoolProperty,
        EnumProperty,
        FloatProperty,
        )
        
class ExportSchematic(Operator, ExportHelper):
    bl_idname = "export.export_schematic"
    bl_label = "Export schematic file"
    
    filename_ext = ".schematic"
    filter_glob: StringProperty(default="*.schematic", options={'HIDDEN'})
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        from . import export_schematic
        return export_schematic.save_schematic(context,
                                          self.filepath)

def menu_func_export(self, context):
    self.layout.operator(ExportSchematic.bl_idname, text="Schematic (.schematic)")


def register():
    bpy.utils.register_class(ExportSchematic)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)
    print("Hello world!")


def unregister():
    bpy.utils.unregister_class(ExportSchematic)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
    
if __name__ == "__main__":
    register()

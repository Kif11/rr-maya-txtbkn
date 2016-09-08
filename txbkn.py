import pymel.core as pm
from pymel.core import PyNode
from pymel.all import mel

class VrayBakeTexures(object):

    def __init__(self):
        self.selection = pm.ls(selection=True)
        self.output_texture_path = '/Users/kif/Documents/rr/dev/maya_txbkn/test/simple_cube/renders'
        self.image_width = 50
        self.cur_version_string = 'v001'

    def configure_global(self):
        """
        Configure V-Ray global baking options
        """
        bake_options = PyNode('vrayDefaultBakeOptions')

        bake_options.setAttr('filenamePrefix', self.cur_version_string)
        bake_options.setAttr('outputTexturePath', self.output_texture_path)
        bake_options.setAttr('resolutionX', self.image_width)

    def bake(self):
        
        self.configure_global()

        mel.optionVar(1, intValue="vrayBakeType")
        mel.optionVar(0, intValue="vraySkipNodesWithoutBakeOptions")
        mel.optionVar(0, intValue="vrayAssignBakedTextures")
        # mel.optionVar(bake_output_dir, stringValue="vrayBakeOutputPath")
        mel.optionVar(0, intValue="vrayBakeProjectionBaking")

        mel.vrayStartBake()

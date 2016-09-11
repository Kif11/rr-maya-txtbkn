import os
import sys
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('rr_server_path', help='path to royal render server root folder')
args = parser.parse_args()

if sys.platform == 'darwin':
    templates = {
        'script_path': os.path.dirname(os.path.realpath(__file__)),
        'maya_plugin_path': '/Applications/Autodesk/maya2015/Maya.app/Contents/MacOS/plug-ins',
        'rr_server_path': args.rr_server_path
    }
elif sys.platform == 'win32':
    templates = {
        'script_path': os.path.dirname(os.path.realpath(__file__)),
        'maya_plugin_path': args.rr_server_path + '/render_apps/_submitplugins',
        'rr_server_path': args.rr_server_path
    }

files = [
  # (source, destination)
    ('{script_path}/rrSubmit_Maya_2009+.py', '{maya_plugin_path}/rrSubmit_Maya_2009+.py'),
    ('{script_path}/3D02__Maya2012__VRayBake.cfg', '{rr_server_path}/render_apps/_config/3D02__Maya2012__VRayBake.cfg'),
    ('{script_path}/rr_bake_textures.py', '{rr_server_path}/render_apps/scripts/rr_bake_textures.py'),
    ('{script_path}/rr_bakeTextures.mel', '{rr_server_path}/render_apps/scripts/rr_bakeTextures.mel'),
]

def expand_templates(path):
    for k, v in templates.items():
        key = '{%s}' % k
        path = str(path).replace(key, str(v))
    return path

for pair in files:

    src = expand_templates(pair[0])
    dst = expand_templates(pair[1])

    print '[+] Copying %s to %s' % (src, dst)

    shutil.copyfile(src, dst)


print '[+] Done!'

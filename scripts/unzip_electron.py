import os
from zipfile import ZipFile
import shutil

HERE = os.path.dirname(os.path.realpath(__file__))
ROOT = os.path.realpath(os.path.join(HERE, ".."))
ELECTRON_FOLDER = os.path.join(ROOT, "src", "compas_rv2", "web")

os.chdir(ELECTRON_FOLDER)

if os.path.exists("electron"):
    print("Deleting existing electron folder")
    shutil.rmtree("electron")

print("unziping electron")
zf = ZipFile("electron.zip", 'r')
zf.extractall(os.path.join(ELECTRON_FOLDER, "electron"))
zf.close()

assert os.path.exists(os.path.join(ELECTRON_FOLDER, "electron"))

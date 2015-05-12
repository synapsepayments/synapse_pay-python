import os 
versionfile = os.path.join(os.path.dirname(os.path.dirname(__file__)), "../VERSION")
VERSION = open(versionfile).read()
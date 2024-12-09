import os
import code
import folder

d = folder.root_folder()

import rationale_machine_code
rationale_machine_code.rationale_machine_code(d)

cwd = d

def ls():
	folder.ls(cwd)

def cd(pth):
	global cwd
	cwd = folder.folder(cwd, pth)



os.system('cls')
code.interact(local=globals())
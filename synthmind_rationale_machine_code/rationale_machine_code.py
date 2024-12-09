from folder import *


def registers(d):
	root = folder(d, 'registers')
	def write(cwd, pth, dat):
		folder(cwd, pth)['_desc'] = dat

	cwd = folder(root, 'RAX')
	write(cwd, 'name', 'RAX')


def rationale_machine_code(d):
	registers(d)
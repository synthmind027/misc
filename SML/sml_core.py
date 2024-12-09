# Trust the programmer
# Memories are only overwritten, not forgotten.

class sml_core:
	def __init__(self):
		self.data = dict()
		self.data['._chld'] = list()
	
	def mk(self, par, nm):
		chld_pth = f'{par}.{nm}'
		self.data[f'{par}._chld'].append(nm)
		self.data[f'{chld_pth}._chld'] = list()
		self.data[f'{chld_pth}._data'] = None

	def chk(self, pth):
		curr_pth = ''
		for seg in pth.split('.')[1:]:
			if seg not in self.data[f'{curr_pth}._chld']:
				self.mk(curr_pth, seg)
			curr_pth = f'{curr_pth}.{seg}'

	def get(self, pth):
		if not pth[0] == '.': 
			pth = '.'+pth
		self.chk(pth)
		return self.data[f'{pth}._data']

	def set(self, pth, dat):
		if not pth[0] == '.': 
			pth = '.'+pth
		self.chk(pth)
		self.data[f'{pth}._data'] = dat

	# Simple api only for test
	def ls(self, pth):
		if not pth[0] == '.': 
			pth = '.'+pth
		self.chk(pth)
		print(self.data[f'{pth}._chld'])


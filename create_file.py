import os
class CheckFile(object):
	def __init__(self,func):
		self.func = func
		self.top = os.path.expanduser('~') 
		
	def __call__(self,*args):
		filename = args[0]
		filetype = args[1]
		ty = filename.split('.')
		path = None
		flag = 0
		for root, dirs, files in os.walk(self.top):	
			if filetype == 'dirs':
				for tmp in dirs:
					if tmp == filename:
						path = root+'/'+filename
						flag = 1
						break
			elif filetype == 'files':
				for tmp1 in files:
					if tmp1 == filename:
						path = root+'/'+filename
						flag = 1
						break
			
		return path,flag
		
		
		
class CreateFile():

	def getFilename(self):
		filename = raw_input("Enter the File name:")
		print "1.Directory\n2.File"
		dic_type = {'1':'dirs','2':'files'}
		filetype = raw_input("Enter the File type:")
		
		return filename,dic_type[filetype]
			
	@CheckFile	
	def check(filename,filetype):
		pass
		
	def create(self,path,filename,filetype):
		if path[1] == 0:
			if filetype == 'dirs':
				print "Directory Created Successfully"
				os.mkdir(filename)
			else:
				print "File successfully created"
				open(filename,'w+')
				
		else:
			print "Already Exists in %s" % path[0]
			
		
		
if __name__ == '__main__':
	cf = CreateFile()
	values = cf.getFilename()
	path = cf.check(values[0],values[1])
	cf.create(path,values[0],values[1])

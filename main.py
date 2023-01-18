class Human:
	def __init__(self, name):
        self.name = name
        self.force = 5
       	self.humanity = 20
	def live(self):
		print(self.name, 'is alive')
        
class hero (Human):
	def __init__(self,name):
		super().__init__(name)
        self.good = 10
	def live(self):
		print(self.name, 'doing good') 
		print(self.name, 'flourishes') 
        
class villain (Human):
	def __init__(self,name):
		super().__init__(name) 
        self.evil = 10
	def live(self):
		print(self.name, 'doing evil') 
		print(self.name, 'rots')
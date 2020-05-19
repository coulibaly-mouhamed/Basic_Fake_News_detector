

##############################################################
class news():
	def __init__(self,headline,domain):
		self.headline = headline
		self.domain = domain
	
	def __str__(self):
		return '%.2c:%2.c' %(self.domain,self.headline)
class invalid_input(Exception):
	pass

	

#########################################################
#Prevent dealing with 
class not_a_link(Exception):
	pass
	
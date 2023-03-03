class Threeton(object):

	__createKey = object()
	__instances = tuple()
	__instanceCount = 0
	
	def __init__(self, key):
		assert(key == Threeton.__createKey), \
			'Threeton instances can only be created using Threeton.createInstance()'

	@classmethod
	def createInstance(cls):
		if len(cls.__instances) < 3:
			instance = Threeton(cls.__createKey)
			cls.__instances += (instance,)
			cls.__instanceCount += 1

		else:
			count = cls.__instanceCount // len(cls.__instances)
			index = cls.__instanceCount - count * len(cls.__instances)
			instance = cls.__instances[index]
			cls.__instanceCount += 1

		return instance
	

if __name__ == '__main__':
	first = Threeton.createInstance()
	second = Threeton.createInstance()
	third = Threeton.createInstance()
	fourth = Threeton.createInstance()
	fifth = Threeton.createInstance()
	sixth = Threeton.createInstance()
	seventh = Threeton.createInstance()
	initFail = Threeton(0)

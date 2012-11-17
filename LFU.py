from heapq import heappush, heappop

class alg:
	def __repr__(self):
		return "LFU"

	def __init__(self, c):
		# c is cache size
		self.c = c
		self.cn = 0
		self.stored = {}
		self.heap = []  # (dist, key, valid)
		self.hitcount = 0
		self.count = 0

	def setup(self, reqlist):
		# I'm an online algorithm :-)
		pass

	def get(self, key):
		self.count += 1
		if key in self.stored:
			self.hitcount += 1
			old = self.stored[key]
			old[2] = False
			item = [key, old[1]+1, True]
			heappush(self.heap, item)
		else:
			self.put(key)

	def put(self, key):
		if key not in self.stored:
			if self.cn == self.c:
				valid = False
				delkey = None
				while not valid:
					dist, delkey, valid = heappop(self.heap)
				del self.stored[delkey]
			else:
				self.cn += 1
			item = [key, 1, True]
			heappush(self.heap, item)
			self.stored[key] = item
from time import sleep

class Clock(object):

	def __init__(self, hour=0, minute=0, second=0):
		self._hour = hour   
		self._minute = minute
		self._second = second


	def run(self):
		self._second += 1
		if self._second == 60:
			self._second = 0
			self._minute += 1
			if self._minute == 60:
				self._minute = 0
				self._hour += 1
				if self._hour == 24:
					self._hour = 0


	def show(self):
		# A = str(self._hour)
		# if self._hour <10:
		# 	A = "0" + A
		# B = str(self._minute)
		# if self._minute <10:
		# 	B = "0" + B
		# C = str(self._second)
		# if self._second <10:
		# 	C = "0" + C
		# return A + ":" + B + ":" + C
		return "{:0>2d}:{:0>2d}:{:0>2d}".format(self._hour, self._minute, self._second)


def main():
	clock = Clock(23, 59, 57)
	while True:
		print(clock.show())
		sleep(1)
		clock.run()

if __name__ == '__main__':
    main()
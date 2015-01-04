#!/usr/bin/python 

import threading 
import time 

class myThread (threading.Thread):
	def __init__ (self, threadID, name, counter):
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print "Starting" + self.name
		#get lock 
		threadLock.acquire()
		print_time(self.name, self.counter, 3)
		#Free lock to release next thread 
		threadLock.release()

def print_time(threadName, delay, counter):
	while counter:
		time.sleep(delay)
		print "%s: %s" % (threadName, time.ctime(time.time()))
		counter -= 1

threadLock = threading.Lock()
threads = []

#create new threads 
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "thread-2", 2)

#Start new threads
thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

#Wait for threads to complete 
for t in threads:
	t.join()
print "Exiting"
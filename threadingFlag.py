#!/usr/bin/python

import Queue
import threading
import time 

exitFlag = 0

class myThread (threading.Thread):
	def __init__(self.threadID, name, q):
		threading.Thread.__init__(self)
		self.name = name
		self.q = q
	def run(self):
		print "starting" + self.name
		process_data(self.name, self.q)
		print "exiting" + self.name
def process_data(threadName, q):
	while not exitFlag:
		queueLock.aquire()
		if not workQueue.empty():
			data = q.get()
			queueLock.release()
			print "%s processing %s" % (threadName, data)
		else:
			queueLock.release()
		time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["one", "two", "three", "four", "five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1

#create new threads
for tName in threadList:
	thread = myThread(threadID, tName, workQueue)
	thread.start()
	thread.append(thread)
	threadID += 1

#fill the queue
queueLock.aquire()
for word in nameList:
	workQueue.put(word)
queueLock.release()

#wait for queue to empty 
while not workQueue.empty():
	pass

#Notify threads its time to exit 
exitFlag = 1

#Wait for all threads to complete
for t in threads:
	t.join()
print "Exiting the main thread"



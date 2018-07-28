from threading import Thread

threads = []

def createThread(func, arg):
    thread = Thread(target=func, args=(arg,))
    # Read each inner list
    # Read name of thread stored there
    # if name === func, 
    threads.append(thread)

def startThread(thread):
    thread.start()

def startAllThreads():
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

def clearThreads():
    global threads
    threads = []


















# class TaskQueue(Queue.Queue):
#     def __init__(self, num_workers=1):
#         Queue.Queue.__init__(self)
#         self.num_workers = num_workers
#         print 'Initiated TQ with ' + str(num_workers) + ' workers'
#         self.startWorkers()
    
#     def addTask(self, task, *args, **kwargs):
#         args = args or ()
#         kwargs = kwargs or {}
#         self.put((task, args, kwargs))
    
#     def startWorkers(self):
#         print 'STARTING WORKER'
#         for i in range(self.num_workers):
#             t = Thread(target=self.worker)
#             print '>> Added new thread ' + str(t)
#             t.daemon = True
#             t.start()

#     def worker(self):
#         while True:
#             item, args, kwargs = self.get()
#             item(*args, **kwargs)
#             self.task_done()
#             # print 'Task Done'

# # def tests():
# #     def blokkah(*args, **kwargs):
# #         time.sleep(5)
# #         print "Blokkah mofo!"

# #     q = TaskQueue(num_workers=5)

# #     for item in range(10):
# #         q.addTask(blokkah)

# #     q.join()       # block until all tasks are done
# #     print "All done!"

# # if __name__ == "__main__":
# #     tests()

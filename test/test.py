import time
#from multiprocessing import Process
import multiprocessing

myFile = './test.log'
start_time = time.time()

def processLine():
  for line in open(myFile):
    if line.find('###') != -1 or line.find('STMT_END_F') != -1:
      yield line
resList = processLine()
fileOut = open('./new.log','w+')
for i in resList:
  fileOut.write(i)

fileOut.close()
mid_time = time.time()
print "1: ", mid_time - start_time ," seconds"

##############################################
fileOut2 = open('./new2.log','w+')
with open(myFile) as tmpFile:
  for line in tmpFile:
    if line.find('###') != -1 or line.find('STMT_END_F') != -1:
      fileOut2.write(line)
fileOut2.close()
last_time = time.time()
print "2: ", last_time - mid_time ," seconds"

#############################################
def works_multi_process(func, worknum):
    proc_record = []
    for i in range(worknum):
        p = multiprocessing.Process(target = func, args = (i,))
        p.start()
        proc_record.append(p)
    for p in proc_record:
        p.join()

def myfunc(fileP):
  with open(fileP) as tmpFile:
    fileOut3 = open('./new3.log','w+')
    for line in tmpFile:
      if line.find('###') != -1 or line.find('STMT_END_F') != -1:
        fileOut3.write(line)
    fileOut3.close()

works_multi_process(myfunc('./test.log'),2)
print "3: ", time.time() - last_time  ," seconds"



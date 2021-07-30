import sched, datetime, time, os
x = datetime.datetime.now()
print("Start_Time = ", x )
s = sched.scheduler(time.time, time.sleep)
#File create
#os.remove("test.txt")
if os.path.isfile("test.txt"):
    file = open("test.txt","a")
else:
    file = open("test.txt", "x")

def add_newLine(sc): 

    print("...Add a New line...", datetime.datetime.now())
    if os.stat("test.txt").st_size == 0:
        with open("test.txt","w") as file1:
            file1.write("Added a New line at time : "+str(datetime.datetime.now())+ "\n")
    else:
        with open("test.txt","a") as file1:
            file1.write("Added a New line at time : "+str(datetime.datetime.now())+ "\n")
    s.enter(1, 1, add_newLine, (sc,))

s.enter(1, 1, add_newLine, (s,))
s.run()

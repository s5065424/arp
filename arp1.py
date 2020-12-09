import pandas as pd
import multiprocessing
import time
import datetime
import random
import string
# for the input of the data from the user.
a = int(input("Enter 1st num -> "))
b = int(input("Enter 2nd num -> "))
sums = a+b
seconds =[]
values=[]
timestamp = []
rand = []
a = time.monotonic()
# For creating time stamp in .xlsx file 
while 1:
    b = time.monotonic()
    ct = str(datetime.datetime.now())
    #ct = ct[0:19]
    #For creating random letters.
    ch = random.choice(string.ascii_letters)
    if((ch>='a' and ch<= 'y') or (ch>='A' and ch<='Y')):
        sums+=1
        seconds.append(str(b-a)[0:1])
        values.append(sums)
        timestamp.append(ct)
        rand.append(ch)
        print(sums)
# User can change the letter.
    if(ch == 'z' or ch == 'Z'):
        df = pd.DataFrame.from_dict({'TimeStamp':timestamp,'random letters':rand,'Sum Value increment of (a+b)':values})
        df.to_excel('exported.xlsx', header=True, index=False)
        quit()
    

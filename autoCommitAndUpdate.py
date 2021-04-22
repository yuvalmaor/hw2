import os
from datetime import datetime
try:
    os.system("git init")
except:
    print("all ready exist")
os.system("git remote add hww https://github.com/yuvalmaor/hw2")#link to repo#new 
os.system("git pull hww")
os.system("git add --all")
os.system('git commit -m "new commit '+str(datetime.now())+'"')
os.system("git push --set-upstream --force hww")

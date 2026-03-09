import shutil
shutil.copy("poet.txt","poet_backup.txt")


import os 
os.remove("poet.txt")
os.remove("poet_backup.txt")
import shutil
shutil.move("poet.txt", "Work/Poems/Russian")


import shutil 
shutil.move("Work/Poems/Russian/poet.txt","Work/Poems/")


import os

for f in os.listdir("Work/Poems"):
    if f.endswith(".txt"):
        print(f)


import shutil
shutil.copy("Work/Poems/poet.txt","Work/Poems")


import shutil
shutil.copy("Work/Poems/poet.txt","Work/Poems/Russian")


import shutil
shutil.move("Work/Poems/Russian","Work/")
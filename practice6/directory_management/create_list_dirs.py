import os
os.makedirs("Work/Poems/Russian")

with open("poet.txt","w", encoding="utf-8") as f:
    f.write("""Я помню чудное мгновенье:
Передо мной явилась ты,
Как мимолетное виденье,
Как гений чистой красоты.

В томленьях грусти безнадежной,
В тревогах шумной суеты,
Звучал мне долго голос нежный
И снились милые черты.
 Aлександр Пушкин""")
    

import os
print(os.listdir("Work/Poems/Russian")) 
# we can not just write os.listdir("Russian") whereas just "Work" is allowed
# because Russian is subfolder and current active folder is directory_management.



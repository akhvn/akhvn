import os
from pathlib import Path

def write_array(arr, file_name):
    for i in range(len(arr)):
       arr[i]+='\n'
    file_name.writelines(arr)

pth = Path("for_main")
f = list(pth.glob('**/*.py'))
S = set()
for p in f:
    S.add(p.parts[-2])
lst = list(S)
lst.sort()
with open("third_out.txt", "w") as f3:
    write_array(lst, f3)
 #the result's in third_out.txt

S = input()
import string
dict={}
list=[]
for i in range(len(string.ascii_lowercase)):
  dict[string.ascii_lowercase[i]]=string.ascii_lowercase[i-3]
for i in range(len(string.ascii_uppercase)):
  dict[string.ascii_uppercase[i]]=string.ascii_uppercase[i-6]
for ch in S:
  if ch in dict:
    list.append(dict[ch])
  else:
    list.append(ch)
for j in range(len(list)):
  print(list[j],end="")
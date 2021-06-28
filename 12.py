a=input("輸入一整數序列為:").split(' ')
tmp=[]
ans=0
for i in a:
    if tmp.count(i)==0:
        tmp.append(i)
for i in tmp:
    if a.count(i) >= len(a)/2:
        ans=i
if ans ==0:
    print("過半元素為:NO")
elif ans != 0:
    print("過半元素為:{}".format(ans))
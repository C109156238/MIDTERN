a=[]
b=[]
x=0
num=(input("please input number:"))
for i in range(len(num)):
    for j in range(len(num),0,-1):
        if len(num[i:j])>=1:
            a.append(num[i:j])
for i in range(len(a)):
    for j in range(1,int(a[i])+1):
        if int(a[i]) % j ==0 :
            x+=1
    if x==2:
        b.append(int(a[i]))
    x=0
b.sort(reverse=True)
if len(b)==0:
    print("prime no found")
else:
    print("子字串中最大的質數值是",b[0])
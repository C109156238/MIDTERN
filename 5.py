M=int(input("請輸入階層值M:"))
tmp=1
for i in range(1,M+1):
    tmp*=i
    if tmp>M :
        print("超過M為%d的最小階層N值為%d"%(M,i))
        break
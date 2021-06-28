q=input("輸入一組四位數字為:")
tmp=''
ans=''
for i in q:
    tmp+=str((int(i)+7)%10)
ans=tmp[2]+tmp[3]+tmp[0]+tmp[1]
print(ans)
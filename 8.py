num1=int(input("請輸入第一行正整數:"))
num2=list(input("請輸入第二行中數列中的數字為:").split(" "))
count=0
countnum=0
for i in num2:
    if int(num2.count(i))>count :
        count=int(num2.count(i))
        countnum=int(i)
if count==1:
    print("每個數字剛好只有一次")
else:
    print("最大出現次數的數字為:%d\n出現次數為:%d"%(countnum,count))
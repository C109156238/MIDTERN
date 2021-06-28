list1=list(input("輸入值為:").split(","))
minx=""
maxx=""
list1.sort()
len1=len(list1)
for i in range(len(list1)):
   minx=minx+list1[i]
list1.sort(reverse=True)
for i in range(len(list1)):
    maxx=maxx+list1[i]
ans=int(maxx)-int(minx)
print("最大值數列與最小值數列差值為:",ans)

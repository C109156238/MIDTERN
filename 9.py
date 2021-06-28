str1=(input("請輸入s1為:"))
str2=input("請輸入s2為:")
yes=0
tmp=""
if len(str1) == len(str2):
        if str1 == str2:
            print("YES")
        else:
            print("NO")
if len(str1) < len(str2):
    for i in range(len(str2)):      #STR1長度小於STR2
        tmp=""
        for j in range(len(str1)):
            tmp+=str2[i+j]
        if str1 == tmp :
            yes+=1
        if i+j == len(str2)-1: #到STR2長度後停止
            if yes >=1:
                print("YES")
                break
            else:
                print("NO")
                break
            
if len(str1) > len(str2):
    print("NO")
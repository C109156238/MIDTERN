#吃兵數
val = list(map(int, input("請輸入遊戲時間：").split(":")))
time = val[0]*60 + val[1] #取得遊戲已進行的時間
time -= 75 - 30 #前01:15
amount = time // 30 #波數
print(F"{amount*6 + amount//3 - amount//2} 隻兵")

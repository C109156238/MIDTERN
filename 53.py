#車資
import math

def main():
    inVal = float(input("請輸入路程公里數(km)："))
    money = calc(inVal)
    print("所需車資為：", money)

def calc(km):
    return int(75 + math.ceil(km-1.5)//0.25 * 5)

main()
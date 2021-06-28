#紙菸
def main():
    n = int(input("請輸入n: "))
    k = int(input("請輸入k: "))
    print("peter可以抽",calc(n, k),"根菸")
    
def calc(a, b, i=0):
    if a+i//b>0: return a + i//b + calc(a//b, b, i%b+a%b)
    else: return 0
main()


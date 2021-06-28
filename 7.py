phone=list(input("輸入月租費型式及通話時間為:").split(","))
if int(phone[0])==186 or int(phone[0])==386 or int(phone[0])==586 or int(phone[0])==986 :
    if int(phone[0]) == 186:
        bill=int(phone[1])*0.09
        if bill <= phone[0]:
            bill*=0.9    
        else:
            bill*=0.8
    if int(phone[0]) == 386:
        bill=int(phone[1])*0.08
        if bill <= int(phone[0]):
            bill*=0.8    
        else:
            bill*=0.7
    if int(phone[0]) == 586:
        bill=int(phone[1])*0.07
        if bill <= int(phone[0]):
            bill*=0.7    
        else:
            bill*=0.6
    if int(phone[0]) == 986:
        bill=int(phone[1])*0.06
        if bill <= int(phone[0]):
            bill*=0.6    
        else:
            bill*=0.5
    print("通話費為:",round(bill))
else:
    print("月租費型式分為186,386,586,986,請輸入正確的月租費用。")

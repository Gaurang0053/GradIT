bal=float(input("Enter the amount:"))

print("1.check balance")
print("2.credit")
print("3.debit")
print("4.exit")
ch=0
while ch!=4:
    ch = int(input())
    if ch==1:
            print("check balance:",bal)
    if ch==2:
            cr=float(input("Enter the amount to credit:"))
            cr=bal+cr
            print("the amount is:",cr)
    if ch==3:
            db = float(input("Enter the amount to debit:"))
            if db>bal+50:
                print("insufficient amount")
            else:
                db=bal-db+50
                print("the debited amount is:", db)
    if ch==4:
     print("Thanku for using our services")




































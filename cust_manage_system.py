class customer:
    print("1.Add Customer:")
    print("2.Delete Customer:")
    print("3.Show all customer:")
    print("4.Update customer:")
    print("5.Exit:")
op=int(input("Please select one option from the given list\n"))
ch = int(input())
while ch!=5:
    if ch==1:
        def addcustomer(self):
            self.name=str(input("enter the name of customer:"))
            self.id=int(input("enter the customer id:"))
            self.no=int(input("enter the customer no:"))
            self.add=str(input("enter the customer address"))
    if ch==2:
        def deletecustomer(id):
            if(self.id==id):
                delete(self.name,self,no,self.add)
            else:
                print("Customer ID not matched with any existing ID")

    if ch==3:
        def showCustomer(self):
            print("the name of customer:",self.name)
            print(" the customer id:",self.id)
            print(" the customer no:",self.no)
            print(" the customer address",self.add)


    if ch==4:
        def updatecustomer(self):
            print("Customer ID : ", self.id)
            self.name = input("Modify customer Name :")
            self.no = input("Modify  customer number :")

    if ch==5:
       exit()



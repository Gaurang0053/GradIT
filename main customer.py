#BLL Code Start From Here
class Customer:
    listCus=[]
    def __init__(self):
        self.id=0
        self.name=""
        self.address=""
        self.mob=""
    def __str__(self):
        return "Id: "+str(self.id)+" Name:"+self.name+" Address:"+self.address+" Mobile No:"+self.mob
    def addCustomer(self):
        Customer.listCus.append(self)
    def searchCustomer(self,id):
        for e in Customer.listCus:
            if(e.id==id):
                self.id=e.id
                self.name=e.name
                self.address=e.address
                self.mob=e.mob
                return
        print("Id not found")#Wrong Code handle it in Exception Handling
    def deleteCustomer(self,id):
        for e in Customer.listCus:
            if(e.id==id):
                Customer.listCus.remove(e)
                return
        print("Id not found")#Wrong Code handle it in Exception Handling
    def modifyCustomer(self,id):
        for e in Customer.listCus:
            if(e.id==id):
                e.id=id
                e.name=self.name
                e.address=self.address
                e.mob=self.mob
                return
        print("Id not found")#Wrong Code handle it in Exception Handling
    @staticmethod
    def showAllCustomer():
        for e in Customer.listCus:
            print(e)
#BLL Code End Here

#PL Code Start From Here
while(True):
    print("1.Add Customer\n2.Search Customer\n3.Delete\n4.Modify\n5.ShowAll\n0.Exit")
    ch=input("Enter your choice")
    if(ch=='1'):
        cus=Customer()
        cus.id=int(input("Enter ID"))
        cus.name=input("Enter Name")
        cus.address=input("Enter Address")
        cus.mob=input("Enter Mobile no")
        cus.addCustomer()
        print("Customer Added Sucessfully")
        #Write Code for Add Customer

    elif(ch=='2'):
        #Write Code for Search Customer
        id=int(input("Enter ID"))
        cus=Customer()
        cus.searchCustomer(id)
        print(cus)
        # print("Id:", cus.id, "Name:", cus.name, "address", cus.address, "mobile No",cus.mob)#Wrong code because list is not available in PL


    elif(ch=='3'):

        #Write Code for Delete Customer
        id = int(input("Enter ID"))
        cus=Customer()
        cus.deleteCustomer(id)
        print("Customer Deleted Sucessfully")


    elif(ch=='4'):
        cus = Customer()
        id = int(input("Enter ID"))
        cus.name = input("Enter Name")
        cus.address = input("Enter Address")
        cus.mob = input("Enter Mobile no")
        cus.modifyCustomer(id)
        print("Customer Modified Sucessfully")

    elif(ch=='5'):
        Customer.showAllCustomer()
        #Write Code for Show All Customer
        pass
    else:
        break


#PL Code End Here
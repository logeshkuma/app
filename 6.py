product=[{"name":"iphone","prize":"45000","stock":"10"},
         {"name":"tv","prize":"30000","stock":"5"}]

cart=dict()
cart1=list()
existinguser=dict()
merchants=dict()
users=dict()
def cart():
     print("cart")
     while True:
          print("1.place order\n 2.cancel")
          s=int(input("select the option"))
          if(s==1):
               print("order placed successfully")
               print("it can delivered within 5 days")
               break
          else:
               print("order cancelled")
               break
                

def buyer():
     print("buyer")
     print("1.search the product\n 2.go to cart")
     h=int(input("choose the option"))
     if(h==1):
          print("search the product")
          search=input("search the product")
          y=0
          for i in product:
               if(search==product[y]["name"]):
                    print("name of the product",product[y]["name"])
                    print("prize of theproduct",product[y]["prize"])
                    while True:
                         print("add cart","or","not")
                         print("1.add\n 2.not add")
                         j=int(input("select the option"))
                         if(j==1):
                              print("add successfully")
                              cart1.append(product[d])
                              return cart()
                         else:
                              print("not added")
                              return
               y+=1
          else:
               return cart()

def vendor():
     while True:
          print("1.New merchant\n2.Existing merchant\n3.exist")
          l=input("enter your choice:")
          if l=="1":
               newmerchant()
          elif l=="2":
               existmerchant()
          elif l=="3":
               break
          else:
               print("invalid input")
          
                               


def admin():
     name="logesh"
     password=5555
     r=input("enter your username:")
     d=int(input("enter your password:"))
     if(r==name and d==password):
         print("Succesfully logged in")
         while True:
             print("1.Approve merchants\n2.Remove merchants\n3.Exit")
             j=int(input("Enter your Choice :"))
             if j==1:
                  approvemerch()
             elif j==2:
                 removemer()
             elif j==3:
                 break
             else:
                 print("Invalid Input")
     else:
         print("Invalid Login credentials")
         input("\tPress Enter to continue")
      
    
    
while True:
    print("welcome to amazon plateform")
    print("1.admin","\n2.vendor","\n3.buyer","\n4.exits")
    a=int(input("enter your  option:"))
    if(a==1):
        admin()
    elif(a==2):
        vendor()
    elif(a==3):
        buyer()
    elif(a==4):
        break
    else:
        print("invalid option")

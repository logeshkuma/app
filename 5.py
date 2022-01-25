total_amount=40000
count=0
k={100:20,200:70,500:40,2000:50}
def admin():
    global total_amount
    name="logesh"
    passcode=1234
    c=input("enter your name:")
    b=int(input("enter your passcode:"))
    if(c==name and b==passcode):
          while True:
              print("1.deposit","\n2.balance check","\n3.exist")
              d=int(input("enter your option"))
              if(d==1):
                  for i in k:
                     print("Enter no .of",i,"notes:")
                     g=int(input())
                     k[i]=k[i]+g
                     total_amount+=g*i
                  print("Your current balance is:",total_amount)
                 
              elif(d==2):
                  print(total_amount)
              elif(d==3):
                  break
              else:
                  print("invalid option")
def user():
    global total_amount,count
    y={2000:0,500:0,200:0,100:0}
    amount=30000
    name="logesh"
    passcode=5555
    h=input("enter your name:")
    while count<3:
        j=int(input("ente your passcode:"))
        if(h==name and j==passcode):
            while True:
                print("1.withdrawl","\n2.balancecheck","\n3.pinchange","\n4.exits")
                v=int(input("enter your option:"))
                if(v==1):
                    s=int(input("enter your amount:"))
                    if(s<total_amount and s%100==0 and s<amount):
                        am=s
                        for i in y:
                            y[i]=am//i
                            am=am%i
                        count1=0
                        for i in y:
                            if(k[i]>y[i]):
                                count1+=1
                        if count1==4:
                            print("take your amount")
                            amount=amount-s
                            print("your account balance is:",amount)
                        else:
                            print("invalid amount in the ATM")
                    else:
                        print("invalid amount")
                            
                    
                elif(v==2):
                    print(amount)
                elif(v==3):
                    r=int(input("enter your old pin:"))
                    w=int(input("enter your new pin:"))
                    print("your pin is changed successfully")
                    passcode==w
                elif(v==4):
                    return
                else:
                    print("invalid option")
        else:
            count+=1
            print("wrong pin")
        print("blocked")                     
            
                  
          

                  
            
          
          

while True:
    print("welcome")
    print("1.user","\n2.admin","\n3.exist")
    a=int(input("enter the option:"))
    if(a==1):
          user()
    elif(a==2):
        admin()
    elif(a==3):
        break
    else:
        print("invalid option")
        
    

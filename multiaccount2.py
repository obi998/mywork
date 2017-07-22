d1 = 0
d2 = 0
d3 = 0
y1 = 0
w1 = 0
pin = 0
class Bank_Account: 
    def pincheck(self, pin):
       if pin in  data:
           return True
       else:
          return False
     # constructor or initializer
    def __init__(self, name, money, pin1):
         self.__name = name
         self.__balance = money   # __balance is private now, so it is only accessible inside the class
         self.__pin = pin1
         

    def deposit(self, money):
         self.__balance += money
 
    def withdraw(self, money):
         if self.__balance > money :
             self.__balance -= money
             return money
         else:
             return "Insufficient funds"
 
    def checkbalance(self):
         return self.__balance
    def next_step():
        while True:
              y2 = int(input("Enter 1 if you want to make a withdrawal, enter 2 if you don't"))
        if y2 == 1:
           enter_pin()
        else:
            print("ERROR, TRY AGAIN")


Bone = Bank_Account('Obi Ezeakachi', 5000, 1111) 
Btwo = Bank_Account('Tasha St.Patrick', 80000 , 2222)
Bthree = Bank_Account('Tommy Egan', 7000, 3333)

data = {Bone:  '1111'  , Btwo :  '2222' , Bthree :   '3333' }
data = {int(pin):value for key, value in data.items()}

def enter_pin():
     while True:
      pin = int( input("Enter pin "))
      if pin == data:
         pincheck()
      else:
       print("INCORRECT PIN TRY AGAIN")

enter_pin()

if Bone.pincheck(pin):
   
   print("Obi Ezeakachi: £",Bone.checkbalance())
   y1 = int(input("Enter 1 if you for a withdrawal, enter 2 if you don't"))
if y1 == 1:
   w1 = input("How much do you want withdraw")
   int(w1)
   print("Withdrawal: £",Bone.withdraw(w1))
   print("Current Balance:",Bone.checkbalance())
   next_step()
else:
   d1 = int(input("How much do you want to deposit"))   
   Bone.deposit(d1)   
   print("Current Balance:",Bone.checkbalance())
   next_step()
if Btwo.pincheck(pin):
   print("Tasha St.Patrick:",Btwo.checkbalance())
y1 = int(input("Enter 1 if you want to make a withdrawal, enter 2 if you don't"))
if y1 == 1:
   w2= int(input("How much do you want to withdraw"))
   print(Btwo.withdraw(w2))
else:
   d2= int(input("How much do you want to deposit"))
   Btwo.deposit(d2)
   print("Current Balance:",Btwo.checkbalance())
   next_step()
if Bthree.pincheck(pin):
    
   print("Tommy Egan:",Bthree.checkbalance())
y1 = int(input("Enter 1 if you want to make a withdrawal, enter 2 if you don't"))   
if y1 == 1:
   w3= int(input("How much do you want to withdraw"))
   print("Withdrawal:",Bthree.withdraw(w3))
   next_step()
else:
   d3= int(input("How much do you want to deposit"))
   Bthree.deposit(d3) 
   print("Current Balance:",Bthree.checkbalance())
   next_step()



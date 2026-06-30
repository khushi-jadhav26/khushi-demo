prompt="enter a name of the city you have visited"
prompt+=" \n I Think You Really enjoy it"
while True:
    city=input(prompt)
    if city=='jaipur':
        break
    else:
        print(f"\n I really enjoyed {city.title()} a lot!!")

number=1
while number<=10:
    print(number)
    number=number+2        

num=0
while num<10:
    num+=1
    if num%2==0:
        continue
    print(num)

num=1
while num<=5:
    print(num)
    num+=1

prompt=("enter a series of pizza toppings")    
while True:
    pizza=input(prompt)
    if pizza=='mushroom':
        break
    else:
        print(f"\n I really like {pizza.title()} topping")     

while True:
    age=int(input("enter a age"))
    if age==6:
        break
    elif age==3:
        print("you don't need money to enter")    
    elif age<=12 :
        print("your entery  ticket cost is 10 rupees")
    elif age>=15:
        print("your  ticket cost is 15 rupees")
    else:
        print("nothing")   

prompt="enter a name of the city you have visited"
prompt+=" \n I Think You Really enjoy it"
active=True
while active:
    city=input(prompt)
    if city=='quit':
        active=False  
    else:
        print(city)    

        

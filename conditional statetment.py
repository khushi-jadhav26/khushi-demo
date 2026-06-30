age_0=18
age_1=22
if age_0>=22  and age_1>=22:
    print(True)
else:
    print(False)

students=['sakshi','aarush']
topper='khushi'
if topper  not in students:
    print(f"{topper.title()}, \n Good Job!!")

car='Toyota'
print("Is car =='Toyota'?I pridict True")
print(car=='Toyota')

age=18
if age>=18:
    print("you are able to vote")
    print("have you registered  to vote?")
else:
    print("your age is not enough to vote")    


age=15
if age<=4: 
    print("your admiision  cost is 0rs ")   
elif age<18:
    print("your admission cost is 25 rs")
else:
    print("your admission cost is 40 rs")

age=3
if age<=4: 
    print("your admiision  cost is 0rs ")   
age_1=12
if 4<=age_1<18:
    print("your admission cost is 25 rs")
age_2=25
if age_2>=18:
    print("your admission cost is 40 rs")

age=20
if age<4:
    prize=0
elif age<18:  
    prize=25 
elif age<21:
    prize=30    
else:
    prize=40
print(f"\n your admission cost is {prize}Rs!")     

colour='red'
if colour=='green':
    print("this symbolises about nature")
if colour=='yellow':
    print("lemon is of yellow colour")
if colour=='red':
    print("this symbolises about  love")

colour='green'
if colour=='yellow':
    print("lemon is of yellow colour")
else:
    print("I like this colour") 

colour='green'
if colour=='green':
    print("this symbolises about nature")

colour='yellow'
if colour=='green':
    print("\n this symbolises about nature")
elif colour=='yellow':
    print("\n lemon is of yellow colour")
else:
    print("\n this symbolises about  love")

person=20
if person<2:
    print("\n the person is baby")
if person>=18:
    print("\n the person is an adult") 
if person>65:
    print("\n the person is elder now ")      

favourite_fruits=['mango','banana','orange']
if 'mango'in favourite_fruits:
    print("\n This is most mouth watering fruit")
if'banana'in favourite_fruits:
    print("\n It is good for health") 
if 'orange'in favourite_fruits:
    print("\n This tastes so fresh anytime")   


pizzas=['cheese','topping']
if pizzas:
    for pizza in pizzas:
        print(f"adding {pizza}")
else:
    print("Are you sure you want plain pizzas?")   



current_users=['khushi','sakshi','aarush','devu']
new_users=['rudra','khushi','shree','sakshi'] 
for new_user in new_users:
    if new_user in current_users:
        print(f"{(new_user.title())} is permanent user") 
    else:
        print(f"{(new_user.title())} is officially new!")    


 


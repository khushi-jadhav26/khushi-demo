class  Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(f"{self.name} is now sitting")
    def roll_over(self):
        print(f"{self.name} rolled over")
my_dog= Dog ("willie",6)
print(f"my dog's name is {my_dog.name}")
print(f"my dog's age is {my_dog.age}")            
my_dog.sit()
my_dog.roll_over()


#Restaurant
class restaurant():
    def __init__(self,name,cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f" \t The restaurant name is {self.name} having cusine type {self.cuisine_type}")
    def open_restaurant(self):
        print(f"\t {self.name} restaurant is open")
Restaurant=restaurant("Tresa","Indian")
print(f"\t  The {Restaurant.name} Restaurant ")
print(f"\t Cuisine type is always {Restaurant.cuisine_type}")
Restaurant.describe_restaurant()
Restaurant.open_restaurant()                

# using 3 different restaurant name
class Restaurant():
    def __init__(self,name,cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"{self.name} is a  most famous restaurant for {self.cuisine_type} cuisine type ")
rest=Restaurant("hyatt","chineese")     
rest1=Restaurant("red chilli","korean")
rest2=Restaurant("gulkand","Indian")
print(f"{rest.name} is fabulous restaurant for {rest.cuisine_type}")
print(f" speciallity of {rest1.name} is {rest1.cuisine_type} type")
print(f"{rest2.name} is best option for {rest2.cuisine_type} food")
rest.describe_restaurant()
rest1.describe_restaurant()
rest2.describe_restaurant()   

#users
class users():
    def __init__(self,first_name,last_name,passion):
        self.first_name=first_name
        self.last_name=last_name
        self.passion=passion
    def describe_users(self):
        print(f"\t {self.first_name} {self.last_name} loves {self.passion}")
    def greet_users(self):
        print(f"\t {self.first_name},Nice to meet you!")
members=users("shree","yadav","football")
print(f"\t Hello,{members.first_name},your {members.passion} practice is amazing ")
members.describe_users()
members.greet_users()       

class car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def discriptive_name(self):
        print(f"{self.year} {self.make} {self.model}")
my_car=car("Audi","a4",2020)
my_car.discriptive_name()  

class car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def discriptive_name(self):
        LONG_NAME=(f"{self.year} {self.make} {self.model}")
        return LONG_NAME.title()
my_car=car("creta","a4",2020)    
print(my_car.discriptive_name())


class car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def describe_car(self):
        print(f"{self.make} {self.model} {self.year}")
    def greet_users(self):
        print(f" This car is {self.odometer_reading} miles far.")
my_car=car("shine","a4",2020)
print(f"{my_car.make} is really shining !")
my_car.describe_car()
my_car.greet_users()        


class fruits():
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
        self.price=0
        
    def describe_fruit(self):
        print(f" \t {self.name} is really tangy in taste !,Having {self.colour} colour. ")
    def nature(self):
        print(f" \t This fruit price is {self.price} rupees per kg.")
my_fruits=fruits("Guava","green")
my_fruits.price=100
my_fruits.describe_fruit()
my_fruits.nature()     

class fruits():
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
        self.price=150
    def describe_fruit(self) :
        print(f" \t {self.name} is really tangy in taste !,Having {self.colour} colour. ")
    def amount(self,rupees):
        self.price+=rupees
    def type(self):
        print(f"This fruit price is {self.price} rupees!")
our_fruit=fruits("Apple","red")
our_fruit.amount(200)
our_fruit.type()
our_fruit.describe_fruit()   


class fruits():
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
        self.price=150
    def describe_fruit(self) :
        print(f" \t {self.name} is really tangy in taste !,Having {self.colour} colour. ")
    def amount(self,rupees):
        self.price+=rupees
    def type(self):
        print(f"This fruit price is {self.price} rupees!")
our_fruit=fruits("plum","red")
our_fruit.type()
our_fruit.amount(40)
our_fruit.describe_fruit ()  


class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self,number):
        print(f" \t The restaurant name is {self.restaurant_name} having cusine type {self.cuisine_type}") 
        self.number_served+=number
    def served(self):
        print(f"The number of customers served was {self.number_served}.") 
restaurant=Restaurant("Tressa","Indian")
restaurant.number_served=30
restaurant.describe_restaurant(50)
restaurant.served()


class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def describe_car(self):
        print(f" \t {self.make} {self.model} {self.year}")
    def structure_car(self):
        print(f"{self.make} car structure changes regulary")
class Electricar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=60
my_car=Electricar("Audi","a4",2019)
my_car.describe_car()
my_car.structure_car()
print(f"\t  This car has {my_car.battery} KWH battery")        
       

class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def describe_car(self):
        print(f" {self.make} {self.model} {self.year}")
    def structure_car(self):
        print(f"{self.make} car structure changes regulary")
class Battery:
    def __init__(self,battery_size=65):
        self.battery_size=battery_size
    def describe_battery(self):
        print(f" {self.battery_size} is battery")    
class Electricar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
my_car=Electricar("Tesla","a4",2018)
my_car.describe_car()
my_car.structure_car()
my_car.battery.describe_battery()  

class Restaurant():
    def __init__(self,name,cuisine_type):
            self.name=name
            self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f" \t The restaurant name is {self.name} having cusine type {self.cuisine_type}")
    def open_restaurant(self):
        print(f"\t {self.name} restaurant is open")
class Icecreamstand(Restaurant):
    def __init__(self,name ,cuisine_type):
        super().__init__(name,cuisine_type)
        self.flavours=[]
    def display(self):
        print("This is the list of the flavours" )
        for flavour in self.flavours:
            print(f"{flavour.title()}")
        
my_flavour=Icecreamstand("mamta","Indian")
my_flavour.flavours=['Butterscotch','vanila','Straberry']
my_flavour.describe_restaurant()
my_flavour.open_restaurant()
my_flavour.display()            




class Restaurant():
    def __init__(self,name,cuisine_type):
            self.name=name
            self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"  The restaurant name is {self.name} having cusine type {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.name} restaurant is open")
class Icecreamstand(Restaurant):
    def __init__(self,name ,cuisine_type):
        super().__init__(name,cuisine_type)
        self.flavours=[]
    def display(self):
        print(f" {self.flavours},this are flavours. ")
        print(f" {self.flavours[0]},this is my favourite.")
my_flavour=Icecreamstand("mamta","Indian")
my_flavour.flavours=['Butterscotch','vanila','Straberry']
my_flavour.describe_restaurant()
my_flavour.open_restaurant()
my_flavour.display()            

class users():
    def __init__(self,first_name,last_name,passion):
        self.first_name=first_name
        self.last_name=last_name
        self.passion=passion
    def describe_users(self):
         print(f"\t {self.first_name} {self.last_name} loves {self.passion}")

    def greet_users(self):
        print(f"\t {self.first_name},Nice to meet you!")
class Admin(users):
    def __init__(self,first_name,last_name,passion):
        super().__init__(first_name,last_name,passion)
        self.privileges=['can add post','can delet post','can ban user']
    def show_privileges(self):
        for privilege in self.privileges:
            print(f" {privilege.title()}")
my_admin=Admin("Khushi","Jadhav","Learning")
my_admin.describe_users()
my_admin.greet_users()
my_admin.show_privileges()  


class users():
    def __init__(self,first_name,last_name,passion):
        self.first_name=first_name
        self.last_name=last_name
        self.passion=passion
    def describe_users(self):
        print(f"\t {self.first_name} {self.last_name} loves {self.passion}")
    def greet_users(self):
        print(f"\t {self.first_name},Nice to meet you!")
class Privileges():
    def __init__(self):
        self.privileges=['can add post','can delet post','can ban user']
    def show_privileges(self):
        for privilege in self.privileges: 
            print(f"{privilege.title()}")  
class Admin(users):
    def __init__(self,first_name,last_name,passion):
        super().__init__(first_name,last_name,passion)   
        self.privileges=Privileges()
my_admin=Admin("Sakshi","Jadhav","Music")
my_admin.describe_users()
my_admin. greet_users()
my_admin.privileges.show_privileges()








# This program shows how to use functions

def guests_list():
    print("welcome!")
guests_list()    

def student_list(username):
    print(f" \n {username.title()},welcome!")
student_list('khushi')   

def favourite_book(name,type):
    print(f"\n{name.title()} is my favourite {type} book!")
favourite_book('ikigai','japaneese')   

#multiple function
def animal(type,animal_name):
    print(f"I have {type}")
    print(f"My {type} name is {animal_name}!")
animal('cat','kitty')
animal('dog','puppy')   

def book(language,name='ikigai'):
    print(f"I have {language}  book")
    print(f"{name.title()} is {language} book!")
def game(type ,name):
    print(f"{name.title()} is {type} game")    
book('japaneese') 
game('indoor','chess')   

def book(language='English',name='ikigai'):
    print(f"I have {language}  book")
    print(f"{name.title()} is {language} book!")
book()    

# positional arguments and keyword arguments
def make_shirt(size,message):
    print(f"The size of the shirt is {size} with message {message}")
make_shirt('large','welcome') 
make_shirt(size='large',message='hello')   

def make_shirt(size='large',message='I love python'):
    print(f" The size of shirt is {size} with message {message}")
make_shirt()
make_shirt('small')
make_shirt('Not_fixed','welcome')    

def describe_city(name='akola',location='maharashtra'):
    print(f"{name.title()} is in {location}")
describe_city()   
describe_city(location='shegaon')
describe_city('vrindawan','gujarat') 

#By returning value

def get_formatted_name(first_name,last_name,middle_name='king'):
    if middle_name:
        full_name=f"{first_name}  {middle_name} {last_name}"
    else:
        full_name=f"{first_name} {last_name}"
    return full_name.title()
musician=get_formatted_name('arijit','singh')
print(musician)
musician=get_formatted_name('arijit', '','singh'  )    
print(musician)

def get_formatted_name(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("tell me your name")
    first_name=input(" \n name :")
    if first_name=='p':
        break
    last_name=input(" \n l_name:")
    if last_name=='q':
        break
    formatted_name=get_formatted_name(first_name,last_name)
    print(formatted_name)



def city_country(city,country):
    place=f"{city} ,{country}"
    return place.title()
location=city_country('buldhana','india')
print(location)
location=city_country('santiago','chile')    
print(location)
print(city_country('vrindhavan','india'))

def make_album(artist_name,album_title,songs=None):
   album= {'artist':artist_name.title(),'title':album_title.title()}
   if songs:
      album['songs']=songs
   return album
album1=make_album('someone','discovery')
print(album1)
print(make_album('new','discovery'))  

def make_album(artist_name,album_title,songs=None):
   album= {'artist':artist_name,'title':album_title}
   if songs:
      album['songs']=songs
   return album
while True:
    print("tell the album details")
    artist_name=input('name :')
    if artist_name=='p':
        break
    album_title=input('title :')
    if album_title=='q':
        break
    album_dic=make_album(artist_name,album_title)
    print(album_dic)        


def greet_users(names):
    for name in names:
        print(f"Hello ! {name.title()}")
usernames=['govinda','shreekrishna']    
greet_users(usernames)     






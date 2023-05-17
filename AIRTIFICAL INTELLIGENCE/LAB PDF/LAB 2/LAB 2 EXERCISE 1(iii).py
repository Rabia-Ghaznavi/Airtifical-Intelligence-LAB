username=input('Enter UserName : ')
user_password=input('Enter User Password : ')
Password='abc$123'
if(Password==user_password.lower()):
    print("Welcome! ")
else:
    print("I don't know you")

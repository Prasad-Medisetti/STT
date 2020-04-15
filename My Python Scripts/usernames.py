uname = ['aditya', 'admin']
pwd = ['Aditya@123', 'admin']

#username = input("Enter Username: ")
#password = input("Enter Password: ")
#if username in uname:
#    id = uname.index(username)
#    if password == pwd[id]:
#        print("Valid Username and Password")
#    else:
#        print("Invalid Password")
#else:
#    print("User Does'nt Exist...")

# Another Way
l = list(zip(uname, pwd))
username = input("Enter Username: ")
password = input("Enter Password: ")
if (username, password) in l:
    print("Valid Username and Password")
else:
    print("Invalid Username or Password")
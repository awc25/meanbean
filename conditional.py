name = input("What's your first name? ")
# the "if" is called a "conditional statement"
# we need to use two equal-signs when doing a test (but only one when doing an assignment)
# if name == "Andrew":
#    print("ok cool, hi")
# else:
#    print("not allowed.  okbye!")
#    exit(1)  # this exits the program immediately

# password = input("What's the secret password? ")
# if password == "arwenisacat":
#    print("good guess")
# else:
#    print("wrong password!")
#    exit(1)  # exit immediately

# if the name and password are OK, you get this secret message
# print("***GONGRAGULATION***")
# print("***HERE ARE THE SECRETS***")
# print("TODO: put secrets here")

# TODO:
# Try a few different name / password combinations.
# Can you tell from the code what name and password are required to unlock the secret message?

if name == "Emily":
    print("Hi Emily")
elif name == "Andrew":
    print("Hi Andrew")

else:
    print("I don't like your name")
    exit(1)

password = input("What's the secret password?  ")
if password == "lyraisacat":
    print ("Welcome")
elif password == "arwenisacat":
    print ("Welcome")
else:
    print("incorrect password! Beep,Beep,Beep!")
    exit(1)
if name == "Emily":
    print ("Hello Emily, have a great day!")
elif name == "Andrew":
    print ("Hello Andrew, I know all your secrets!")



# TODO: modify this so that:
# 1. it will also accept your name (in addition to "Andrew")
# 2. it will accept both "arwenisacat" and "lyraisacat" as a password (no matter what name)
# 3. it prints out different secret messages (of your choice) depending on the name

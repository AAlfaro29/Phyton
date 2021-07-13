#4
#program asks th euser for their height,and determines whether or not they are tall enough to ride the rollercoaster
#height = int(input("What is your height in cms? "))

#if height >= 120:
    #print("Hop on!")
#else:
    #print("Sorry, not today.")

#5
# program that asks the user to enter their username and password,and outputs a success message if they are correct, or a failure message
user1 = str("fleur")
password1 = str("password123")

user = str(input("What is your user name? "))
password = str(input("What is your password? "))


if user1 == user and password1 == password:
    print("Correct!")

else:
    print("Incorrect!")
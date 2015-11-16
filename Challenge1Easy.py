'''
    Author: Juan A. Uribe
    Date: November 16, 2015
    Description: Reddit Daily Programmer Challenge #1
    Ask user to enter name, age and reddit username
'''

name = input("Enter your name: ")
age = input("Enter your age: ")
ruser = input("Enter your reddit username: ")

message = "Your name is "  + name + ", you are " + age \
          + " years old, and your user name is " + ruser

print (message)

f = open("output.txt", "w")

for item in message:
    f.write(str(item))

f.close()
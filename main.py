
name = input("firstname: ")
print("your name is: " + name)
item = input("what do you wish to have " + name + " there is black coffee, tea, milk:")
print("you have selected: " + item)
review = input("please rate us " + name + " out of 10:")
if int(review) > 5:
    print("Feel welcome again")
else:
    print("Goodbye and thank you")
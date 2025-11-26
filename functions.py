#A function to greet the user by name
#def greeting(name):
  #print(f"Welcome {name}. How are you doing today?")

#greeting("Tevin")

#A function to calculate the area of a rectangle
#def area_rectangle(length, width):
    #return length * width

#length = int(input("What is the length of the rectangle? "))
#width = int(input("What is the width of the rectangle? "))

#print(area_rectangle(length, width))

#A function to check if a number is odd or even
def odd_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

number = int(input("What number can we check for you today? "))
result = odd_even(number)

print(f"Your number is {result}")
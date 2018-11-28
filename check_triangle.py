print("\nProgram to test Three inputs to See if they form a triangle")
print("Please enter input length of triangle :  ")
x = int(input("Enter the dimension of side x: "))
y = int(input("Enter the dimension of  side y: "))
z = int(input("Enter the dimension of side z: "))


# Function to check whether a given values form triangle and display its name
def print_name():
    if x != y and y != z and x != z:
      print("Scalene")
    elif x == y and y == z:
        print("Equilateral")
    else:
      print("Isosceles")


# Using
# Triangle Inequality Theorem :
# a + b > c , a + c > b, c + b > a
while x + y > z and x + z > y and y + z > x:
  print("\nThe shape is a triangle: ")
  print_name()
  break
else:
   print("\nEntered dimensions do not form a triangle based on Triangle Inequality Theorem")
   print("Please try again")

























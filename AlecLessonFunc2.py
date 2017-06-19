def f():
    x = 22
    print(x)
# Call the function
f()
# This fails, x only exists in f()
#print(x)


# Create the x variable and set to 44
x = 44
 
# Define a simple function that prints x
def f():
    print(x)
 
# Call the function
f()


def f(x):
    x += 1
    print(x)
 
# Set y
y = 10
# Call the function
f(y)
# Print y to see if it changed
print(y)


def f(x):
    x += 1
    print(x)
 
# Set x
x = 10
# Call the function
f(x)
# Print x to see if it changed
print(x)


def main():
    print("Hello world.")
 
main()


def main():
    print("Hello world.")
 
if __name__ == "__main__":
    main()

#Question 1 í dæmatíma um git
num_int = int(input("Input a number: "))    # Do not change this line
num_max = 0 

while num_int >=0:
    num_int = int(input("Input a number: ")) 

    if num_max < num_int:

        num_max = num_int 

print("The maximum is", num_max) 
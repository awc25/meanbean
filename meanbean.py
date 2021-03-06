# anything starting with the pound-sign is a comment

# if you want to print out a string, it must be in quotes
print("beans, beans, beans")
print("Lyra, Lyra, Lyra")

# define variables with single equal sign
num_rows = 20
num_columns = 8

# the %d is used to print a number
print("there are %d rows" % (num_rows))

# there are two %d - therefore, you need two numbers
print("there are %d rows and %d columns" % (num_rows, num_columns))

# TODO: find the total number of cells in the grid
num_cells = num_rows * num_columns
print("The total number of cells is... %d" % (num_cells))

# use * for multiplication
# assign the result to a new variable, num_cells
# then print this out with a nice message

# Just as you use %d to print an integer,
# you can use %s to print a string:
firstname = "Ren"
lastname = "Stimpy"

print("the names are %s%s" % (firstname, lastname))
# notice how this squishes together the two names -> RenStimpy
# because there was no space between the %s and the other %s

# TODO: store your first and last names as variables
firstname = "Emily"
lastname = "Martin"
print("My name is %s %s" % (firstname, lastname))
print("My name is %s, %s" % (lastname, firstname))

# then print your name in two different ways,
# one with last name first and the other with first name first
# use fake names and disguise your voice

# hi Emily is here
firstname = "Lyra"
lastname = "Martin"
print("My name is %s %s" % (firstname, lastname))
print ("%s is the best cat that the %s's ever owned" % (firstname, lastname))
print ("the %s's the best owner that %s's ever ruled over" % (lastname, firstname))
print ("%s is the queen of the house" % (firstname))

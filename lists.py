# Here is how you create a "list" in Python:
invited_people = ["Arwen", "Fatima", "Andrew", "Lyra"]

# Here is how to see the third element in the list:
# Why did I say "2" and not "3"?
print("The fourth element is: %s" % invited_people[3])

# Here is how you add something to the end of a list.
# Notice the use of the dot here.
invited_people.append("Stimpy")
invited_people.remove("Arwen")
invited_people.append("Emily")

# A string in python is itself a list - a list of individual characters!
# Here, I print out the second letter in a string
# Use the %c to print a character
my_name = "Beavis"
print("The first letter of my name is: '%c'" % my_name[0])
# The "-1" index gives you the last element of a string:
print("The last letter of my name is: '%c'" % my_name[-1])

# Here is how you can "iterate" over a list.
# "Iterate" means to "loop through" all of the elements of the list.
# invited_people is the list.
# person is a variable whose value changes as you iterate.
for person in invited_people:
#    print("%s in invited." % person)
    print("%c is first letter" % person [0])


# You can get the length of a list like this:
print("A total of %d people are invited." % len(invited_people))
print("Let's see if you are on the list.")

# You can check if something is in a list using "in", like this:
name = input("Enter your name: ")
if name in invited_people:
    print("Cool, you are invited!")
else:
    print("Not invited OKBYE!")
    exit(1)

# TODO:
# 1. Notice how Stimpy was added to the list after the others.
#    See if there is a way to "remove" names from the list.
#    Remove Arwen from the list using "remove".
# 2. Add yourself to the list using "append".
# 3. Print the list before and after each addition and removal.
# 4. Print the first initial of each invitee.
#    There is an example of iterating through all the invited people above.
#    There is also an example of how to get the first letter of a string above.

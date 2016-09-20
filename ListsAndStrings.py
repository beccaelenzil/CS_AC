# python 2
#
# Name:
#
# Homework 2, Problem 1a and 1b
# slicing and indexing challenges: Lists and Strings
#

pi = [3,1,4,1,5,9]
e = [2,7,1]

# Example problem (problem 0):
# Creating the list [2,5,9] from pi and e
answer0 = [ e[0] ] + pi[-2:]
print answer0


#problem 1:
#Creating the list [7,1] from pi and/or e
answer1 = e[1:]
print answer1

#problem 2:
#Creating the list [9,1,1] from pi and/or e
answer2 = pi[5:0:-2]
print answer2

#problem 3:
#Creating the list [1,4,1,5,9] from pi and/or e
answer3 = pi[1:]
print answer3

#problem 4:
#Creating the list [1,2,3,4,5] from pi and/or e
answer4 = [e[-0:-3:2]]+

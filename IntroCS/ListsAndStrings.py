# python 2
#
# Name: Alison Cohen
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
answer4 = e[3::-2] + pi[::2]
print answer4

h = 'harvey'
m = 'mudd'
c = 'college'

# problem 5:
# Creating the string 'heyyou'
answer5 = h[0] + h[4:] + h[-1] + c[1] + m[1]
print answer5

#problem 6
#Creating  the string 'collude'
answer6 = c[:4] + m[1:3] + c[4:5]
print answer6

#problem 7
#Creating the string 'arveyudd'
answer7 = h[1:] + m[1:]
print answer7

#problem 8
#Creating the string 'hardeharharhar'
answer8 = h[:3]+m[2:3]+h[4:5]+ h[:3]*3
print answer8

#problem 9
#Creating the string 'legomyego'
answer9 = c[3:6] + c[1:2] + m[:1] + h[5:] + c[4:6] + c[1:2]
print answer9

#problem 10
#Creating the string 'clearcall'
answer10 = c[:5:2] + h[1:3] + c[:1] + h[1:2] + c[2:4]
print answer10


p = 'harry potter'
g = 'hermione granger'
w = 'ron weasley '
m = 'draco malfoy'

#problem 11
#Creating the string 'ginny weasley is cool'
answer11 = g[9::-5] + g[6:7]*2 + w[10:] + w[4:] + g[4:5] + w[7::4] + m[3:5] + m[4:9:4]
print answer11

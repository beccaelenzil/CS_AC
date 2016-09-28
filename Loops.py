#problem one
def power(b,p):
    """
    ouput: b^p
    input: two integers
    """
    result = 1
    for i in range (0,p):
        result = result*b
    return result

print "power(2,5): should be 32 == ", power(2,5)
print "power(5,2): should be 25 == ", power(5,2)
print "power(42,0): should be 1 == ", power(42,0)
print "power(0,42): should be 0 == ", power(0,42)
print "power(0,0): should be 1 == ", power(0,0)


#problem two
def summedOdds( L ):
    """
        input: L, a list of integers
        output: the sum of the odd numbers in list L
    """
    result = 0

    for e in L:
        if e%2 == 0:
            result = result
        else:
             result += e
    return result

# tests!
print "summedOdds( [4,5,6] ): should be 5 == ", summedOdds( [4,5,6] )
print "summedOdds( range(3,10) ): should be 24 == ", summedOdds( range(3,10) )

#problem three
def mult(n,m):
    """
    input: two integers
    output: the product of the two integers
    """

    result = 0
    for i in range(0,abs(m)):
        if m > 0:
            result = result + n
        else:
            result = result - n
    return result

print "mult(6,7)    42 ==", mult(6,7)
print "mult(6,-7)  -42 ==", mult(6,-7)
print "mult(-6,7)  -42 ==", mult(-6,7)
print "mult(-6,-7)  42 ==", mult(-6,-7)
print "mult(6,0)     0 ==", mult(6,0)
print "mult(0,7)     0 ==", mult(0,7)
print "mult(0,0)     0 ==", mult(0,0)

#problem four
def dot( L, K ):
    """
    input: two lists
    output: the dot product of the lists
    """

    result = 1
    for i in range(0 ,L[:]):
        



print "dot( [5,3], [6,4] )     42.0 ==", dot( [5,3], [6,4] )
print "dot( [1,2,3,4], [10,100,1000,10000] )  43210.0 ==", dot( [1,2,3,4], [10,100,1000,10000] )
print "dot( [5,3], [6] )        0.0 ==", dot( [5,3], [6] )
print "dot( [], [6] )           0.0 ==", dot( [], [6] )
print "dot( [], [] )            0.0 ==", dot( [], [] )

"""
Link to trinket file: https://trinket.io/python/3509bbf5ce
"""

def fib(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print "fib(5) == 5 = ",fib(5)," : ", 5 == fib(5)
print "fib(11) == 89 = ",fib(11)," : ", 89 == fib(11)

def fibIter(n):

    fibSeq = [0,1]

    for i in range(2,n+1):
        fibSeq.append(fibSeq[i-1]+fibSeq[i-2])
    return fibSeq[i]

print "fibIter(5) == 5 = ",fibIter(5)," : ", 5 == fibIter(5)
print "fibIter(11) == 89 = ",fibIter(11)," : ", 89 == fibIter(11)


def listReverse(L):

    if len(L)== 1:
        return L
    else:
        return [L[-1]] + listReverse(L[0:-1])

def listReverseIter(L):

    listSeq = []

    for i in range(len(L)):
        listSeq.append(L[-1-i])

    return listSeq



print "listReverse([1,2,3,4]) == [4,3,2,1] = ",listReverse([1,2,3,4])," : ",listReverse([1,2,3,4]) == [4,3,2,1]
print "listReverseIter([1,2,3,4]) == [4,3,2,1] = ",listReverseIter([1,2,3,4])," : ",listReverseIter([1,2,3,4]) == [4,3,2,1]

#challenge: binary conversion

def isOdd(n):

    if n%2 == 0:
        return False
    else:
        return True

print "isOdd(45) == True =" , isOdd(45)
print "isOdd(88) == False =" , isOdd(88)


def numToBinary(N):

  if N == 0:
    return ''
  elif N%2 == 1:
    return  numToBinary(N/2) + '1'
  else:
    return  numToBinary(N/2) + '0'


print 'numToBinary(0)==', numToBinary(0), ":", numToBinary(0) ==''
print 'numToBinary(1)==', numToBinary(1), ":", numToBinary(1) =='1'
print 'numToBinary(4)==', numToBinary(4), ":", numToBinary(4) =='100'
print 'numToBinary(10)==', numToBinary(10), ":", numToBinary(10) == '1010'
print 'numToBinary(42)==', numToBinary(42), ":", numToBinary(42) == '101010'
print 'numToBinary(100)==', numToBinary(100), ":", numToBinary(100) == '1100100'

"""
def binaryToNum(S):
  if S == '':
    return 0

  # if the last digit is a '1'
  elif S[-1] == '1':
    return  binaryToNum(S/2) + 1

  else: # last digit must be '0'
    return  binaryToNum(S/2) + 0

print 'binaryToNum(100)==', binaryToNum(100), ":", binaryToNum(100) =='4'
print 'binaryToNum(1011)==', binaryToNum(1011), ":", binaryToNum(1011) =='11'
print 'binaryToNum(00001011)==', binaryToNum(00001011), ":", binaryToNum(00001011) =='11'
print 'binaryToNum("")==', binaryToNum(), ":", binaryToNum() =='0'
print 'binaryToNum(0)==', binaryToNum(0), ":", binaryToNum(0) =='0'
print 'binaryToNum(1100100)==', binaryToNum(1100100), ":", binaryToNum(1100100) =='100'
print 'binaryToNum(101010)==', binaryToNum(101010), ":", binaryToNum(101010) =='42'
"""


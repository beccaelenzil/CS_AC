#Arithmetic Processing

def tpl(x):
  """
  output: tpl returns thrice its input
  input x: a number (int or float)
  """
  return 3*x
print 'tpl(3) is', tpl(3)

#problem 1

def sq(x):
    """
    output: sq returns the square of its inuput
    input x: a number (int or float)
    """
    return x**2
print 'sq(3) is' , sq(3)


#problem 2

def interp(low , high , fraction):
  """
  output: interp prints a number a fraction of the way between low and high
  input: 3 numbers (int or float)
  """
  return (fraction * (high - low)) + low

print 'interp(1,9,0.25) is' , interp(1,9,0.25)


#String Functions

#problem 3

def checkends(s):
    """
    output: True or False
    input: a string
    """
    if s[0] == s[-1]:
        return True
    else:
        return False

print 'checkends(string) is' , checkends('string')
print 'checkends(anna) is' , checkends('anna')

#problem 4

def flipside(s):
    """
    output: flipside prints a string
    input: a string that flips the first and second half of the original string
    """
    x = len(s)/2
    return s[x:] + s[:x]

print 'flipside(homework) is' , flipside('homework')
print 'flipside(carpets) is' , flipside('carpets')

#String and Arithmetic

#problem 5

def convertFromSeconds( s ):
    """
    output: convertFromSeconds prints a string of 4 numbers representing the number of seconds in more conventional units of time
    input: a number of seconds
    """
    days = s / (24*60*60)  # # of days
    s = s % (24*60*60)     # leftover seconds
    hours = s / (60*60) # # of hours
    s = s % (60*60) # leftover seconds
    minutes = s / (60) # # of minutes
    s = s % (60) # leftover seconds
    seconds = s
    return [days, hours, minutes, seconds]

print 'convertFromSeconds(610) is' , convertFromSeconds(610)
print 'convertFromSeconds(100000) is' , convertFromSeconds(100000)

#codingbat
def front3(str):
  return str[:3] * 3

#Challenge

#warm up

def pigletlatin(s):
    """
    output: if starts with vowel, add way. if starts with consonant, add ay
    input: a string
    """
    vowels = ['a','e','i','o','u','A','E','I','O','U']


    if s[0] in vowels :
        return s + 'ay'
    else:
        return s + "way"

print 'pigletlatin(alison) is', pigletlatin('alison')
print 'pigletlatin(diana) is', pigletlatin('diana')


#piglatin
def piglatin(s):
    """
    output: moves initial letter to end. if starts with vowel, add way. if starts with consonant, add ay. determine if vowel/consonant for y.
    input: a string
    """
    vowels = ['a','e','i','o','u','A','E','I','O','U']


    if s[0] is 'y':
        if s[0] in vowels:
            return s + 'way'
        else:
            return s[1:] + s[:1] + 'ay'

    elif s[0] in vowels:
        return s + 'way'
    else:
        for i in range(len(s)):
            if s[i] in vowels:
                return s[i:] + s[:i] + 'ay'

print 'piglatin(string) is', piglatin('string')
print 'piglating(yttrium) is' , piglatin('yttrium')

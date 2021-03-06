'''
Created on May 17, 2012

@author: Rishi Maharaj
'''
import random
from datetime import datetime

class WeakPrng(object):
    def __init__(self, p):   # generate seed with 56 bits of entropy
        self.p = p
        self.x = random.randint(0, p)
        self.y = random.randint(0, p)
   
    def next(self):
        # x_{i+1} = 2*x_{i}+5  (mod p)
        self.x = (2*self.x + 5) % self.p

        # y_{i+1} = 3*y_{i}+7 (mod p)
        self.y = (3*self.y + 7) % self.p

        # z_{i+1} = x_{i+1} xor y_{i+1}
        return (self.x ^ self.y) 
    
class WeakPrngModified(object):
    def __init__(self, p, x, y):   # generate seed with 56 bits of entropy
        self.p = p
        self.x = x
        self.y = y
   
    def next(self):
        # x_{i+1} = 2*x_{i}+5  (mod p)
        self.x = (2*self.x + 5) % self.p

        # y_{i+1} = 3*y_{i}+7 (mod p)
        self.y = (3*self.y + 7) % self.p

        # z_{i+1} = x_{i+1} xor y_{i+1}
        return (self.x ^ self.y)
    
def printIteration(iterationCounter):
    if iterationCounter % 1000 == 0:
        print iterationCounter

#import Cryptography.week1.PRG.WeakPrng

outputs = [210205973, 22795300, 58776750, 121262470, 264731963, 140842553, 242590528, 195244728, 86752752]

#choose value x between 0 and p (at random), see what value of y is needed to get second output.
P = 295075153L
result = []
checked = []
iterationCounter = 0
duplicateCounter = 0
startTime = datetime.now()
x1 = 268435000
print startTime
while True:
    x1 += 1
#    while True:
#        if x1 in checked:
#            print "Duplicate found: " + str(duplicateCounter) + " at iteration: " + str(iterationCounter)
#            duplicateCounter += 1
#            x1 = random.randint(0,P)
#        else:
#            checked.append(x1)
#            break
#    print checked
    x2 = 2*x1 + 5
    y2 = x2 ^ outputs[1]
    y1 = (y2 - 7 )/3
    
    if y1^x1 == outputs[0]:
        print "FOUND:"
        print x1
        print y1
        p1 = WeakPrngModified(P, x1, y1)
        for i in range(1, 11):
            result.append(p1.next())
        if result == outputs:
            print "LAST = "
            print p1.next()
            break
        else:
            result = []
            printIteration(iterationCounter)
            iterationCounter+=1
    else:
        printIteration(iterationCounter)
        iterationCounter+=1
        if iterationCounter > 2**28:
            break
print "Total time taken = " + str(datetime.now()-startTime)


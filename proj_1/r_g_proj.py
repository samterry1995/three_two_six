import random

green = 'g'
red = 'r'
dictionary = {1: green}

def isInDictionary(a):
    if a in dictionary:
        print(dictionary.values())
    else:
        findNearFactors(a)

def calcColor(nearFactors):
    greencount = 0
    print(greencount)
    redcount = 0
    for i in nearFactors:
        if dictionary.get(i) == 'g':
            greencount +=1
            print(greencount)
        elif dictionary.get(i) == 'r':
            redcount += 1
    if greencount > redcount :
        return 'r'
    else:
        return 'g'

def findNearFactors(a):
    almostNearFactors = [ ]
    if a != 2:

        for i in range(a//2, 1, -1):
            print(i)
            almostNearFactors.append(a//i)
            nearFactors = set(almostNearFactors)
            isInDictionary(set[0])

    else:
            two = [1]
            dictionary.update({ 2: calcColor(two)})
    
           # print(a)
  #      if isInDictionary(i) :
          #  return 'yes'
            

def main():
    isInDictionary(10)
    print(dictionary.values())

main()
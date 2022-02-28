#Samuel Terry - 6786350
#Etude 9 Arithmetic Countdown

from queue import LifoQueue
import sys

def left_compute(op_string, numbers):
    i=0
    value = numbers[i]
    for op in op_string:
        if op == "+":
            i+=1
            value = value + numbers[i]
        elif op == "*":
            i+=1
            value = value * numbers[i]
    node_value = value
    return node_value

def normal_compute(op_string, numbers):
    known = 0
    i=0
    pending = numbers[i]
    for op in op_string:
        if op == "+":
            i+=1
            known = known + pending
            pending = numbers[i]
        elif op == "*":
            i+=1
            known = known
            pending = pending * numbers[i]       
    node_value = known + pending
    return node_value

def search(target,numbers, compute_method):
    stack = LifoQueue(maxsize=0)
    stack.put("")
    ops_wanted = len(numbers)-1
    while stack.qsize() > 0:
        op_string = stack.get()
        node_val = compute_method(op_string,numbers)  
        if len(op_string) == ops_wanted:
            if node_val == target:
                return op_string
        elif (node_val <= target):
                stack.put(op_string + "+")
                stack.put(op_string + "*")
    return False

def list_to_string(lst):
    result = str(lst[0])
    for char in lst[1:]:
        result += " " + str(char)
    return result

def main():
    for line in sys.stdin:
        tokens = line.rsplit()
        output = []
        try:
            if tokens[0] == 'N':
                order = tokens.pop(0)
                tokens = list(map(int,tokens))
                answer = tokens.pop(0)
                ops = search(answer,tokens, normal_compute)
                if ops: #If ops true (we didn't get an impossible to solve expression.)
                    output.append(tokens[0])
                    for i in range(len(ops)):
                        output.append(ops[i])
                        output.append(tokens[i+1])
                    print(f'{order} {answer} = {list_to_string(output)}')
                else:
                    print(f'{order} {answer} {list_to_string(tokens)} impossible')
                           
            elif tokens[0] == 'L':
                order = tokens.pop(0)               #Assigns my order of operations char to variable order
                tokens = list(map(int,tokens))      #Turn all the numbers in my list into type int
                answer = tokens.pop(0)              #Grab the answer for my equation and assign to answer variable
                ops = search(answer,tokens,left_compute)    #Grabs the string of operators, if it can't then EXCEPTION
                
                if ops:
                    output.append(tokens[0])                #If I put the first number in then num_operators == num_numbers
                    for i in range(len(ops)):   #Adds an operator then adds a number.
                        output.append(ops[i])
                        output.append(tokens[i+1])
                    print(f'{order} {answer} = {list_to_string(output)}')   #My draft output...
                else:
                    print(f'{order} {answer} {list_to_string(tokens)} impossible')


            else:
                raise Exception()

        except Exception:
            print(f'{list_to_string(tokens)} Invalid')
main()















# There are various functions available in this module: 

# maxsize – Number of items allowed in the queue.
# empty() – Return True if the queue is empty, False otherwise.
# full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
# get() – Remove and return an item from the queue. If the queue is empty, wait until an item is available.
# get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
# put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
# put_nowait(item) – Put an item into the queue without blocking.
# qsize() – Return the number of items in the queue. If no free slot is immediately available, raise QueueFull
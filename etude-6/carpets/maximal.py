__author__ = "Katelyn Harlan (4437710), Taya Nicholas (5926161), Samuel Terry (6786350)"

from collections import deque


def greedy(stock, size):
    """
    Simple greedy algorithm to get a lower bound for a maximal carpet.
    ---
    PARAMS
    stock: [String]
        a list of strings(strips) representing the stock
    size: int
        the number of strips needed in the carpet
    ---
    RETURN
    [String]
        returns a list of strips representing a carpet
    """
    temp_stock = stock.copy() #remove strips from temp_stock when we add to the greedy carpet
    greedyCarpet = list()
    greedyCarpet.append(temp_stock[0])
    temp_stock.pop(0)
    #Build the carpet strip by strip, picking the most matches each time
    while len(greedyCarpet) < size:
        temp_strip = temp_stock[0]
        for strip in temp_stock:
            if (potential_matches(greedyCarpet, strip) > potential_matches(greedyCarpet, temp_strip)):
                temp_strip = strip
        greedyCarpet.append(temp_strip)
        temp_stock.remove(temp_strip)
    return greedyCarpet

def maximal_carpet(stock, size):
    """
    Uses DFS with pruning to find a Carpet with the maximum number of matches.
    ---
    PARAMS
    stock : [String]
        the list of strings representing the strips in our stock
    size : int
        the desired length of the final carpet
    ---
    RETURN
    [String]
        returns a list of strings, representing the maximal carpet
    """
    strip_matches = compute_matches(stock)
    max_carpet = greedy(stock, size) 
    max_matches = total_matches(max_carpet)
    #If we don't have any possible matches within our stock, just return our greedy carpet
    if max_matches == 0:
        return max_carpet 

    stack = deque()
    for strip in stock:
        strips = []
        strips.append(strip)
        stack.append(strips)
    current_carpet = []

    while stack:
        current_carpet = stack.pop()
        total = total_matches(current_carpet)
        #Is it better than our current max carpet?
        if total_matches(current_carpet) > max_matches:
                max_carpet = current_carpet
                max_matches = total_matches(current_carpet)
        if len(current_carpet) >= size:
            continue
        

        #If we had optimal strips for the rest of this carpet, would it be better?
        remaining = size - len(current_carpet)  
        if optimal_matches(remaining, current_carpet, strip_matches, total) < max_matches:
            continue

        #Generate children

        #Remove strips currently in the carpet, but make sure they are kept in order of best matches
        temp_stock = make_temp_stock(current_carpet, strip_matches)

        for strip in temp_stock:
            child = current_carpet.copy()
            child.append(strip)
            stack.append(child)
    return (max_carpet, max_matches)

def optimal_matches(remaining, current_carpet, strip_matches, total):
    """
    Computes the amount of matches the carpet would have if all remaining strips were optimal choices.
    ---
    PARAMS
    remaining : int
        the number of strips remaining for the final carpet
    current_carpet : [String]
        the carpet to find optimal matches for
    strip_matches : dictionary
        the dictionary containing the lists of strips ordered by matches
    total : int
        the total number of matches for the current_carpet
    ---
    RETURN
    int
        returns the number of matches the carpet would have if it were optimal
    """
    matches = total
    carpet = current_carpet.copy()
    previous = current_carpet[-1]
    for _ in range (0, remaining):
        temp_stock = make_temp_stock(carpet, strip_matches) #need to get the order for each new end strip
        matches += find_matches(previous, temp_stock[0])
        carpet.append(temp_stock[0])
        previous = temp_stock[0]
    return matches
  
def make_temp_stock(current_carpet, strip_matches):
    """
    Takes the precomputed list of strips ordered by matches to the end strip of the carpet, and removes the strips currently in said carpet.
    This takes into acoount rotated versions of strips.
    ---
    PARAMS
    current_carpet : [String]
        the list of strips to remove from stock
    strip_matches : dictionary
        the strips ordered by matches
    ---
    RETURN
    [String]
        returns the remaining stock, ordered by matches to the end piece
    """
    #make a temp_stock by removing the current carpet strips from a copy of the dictionary list
    #from the end strip of the current carpet
    #if a strip in our carpet is not in the stock, we try the rotated version
    temp_stock = strip_matches[current_carpet[-1]].copy()
    for index in range (0, len(current_carpet) -1):
            strip = current_carpet[index]
            if strip in temp_stock:
                temp_stock.remove(strip)
            elif strip[::-1] in temp_stock:
                temp_stock.remove(strip[::-1])
    return temp_stock

def compute_matches(stock):
    """
    Takes in the stock and computes all of the matches for each strip (normal and reversed), sorts them by most matches, 
    and gives a dictionary containing this information.
    ---
    PARAMS
    stock : [String]
        the list of all the strips in stock
    ---
    RETURN
    dictionary
        returns a dictionary of all the strips (and their reversed forms), with a list of all the other strips
        ordered by number of matches
    """
    strip_matches = {}
    reverse_stock = list()
    for strip in stock:
        reverse_stock.append(strip[::-1])
    #Calculate the matches for all normal strips
    for outer_index in range (0,len(stock)):
        strip_pairs = list()
        for inner_index in range (0, len(stock)):
            if(outer_index == inner_index):
                continue
            #If the strip we are testing matches better reversed, we will take that version
            normal_matches = find_matches(stock[inner_index],stock[outer_index])
            reverse_strip = stock[inner_index][::-1]
            reverse_matches = find_matches(stock[outer_index],reverse_strip)
            if reverse_matches > normal_matches:
                matches = tuple((reverse_strip,reverse_matches))
            else:
                matches = tuple((stock[inner_index], normal_matches))
            strip_pairs.append(matches)
        #Need to sort by the matches
        strip_pairs.sort(key= lambda x:x[1], reverse=True)
        key_value = list()
        for strip in strip_pairs:
            key_value.append(strip[0])
        strip_matches[stock[outer_index]] = key_value
    
    #Calculate all the matches for the reversed strips
    for outer_index in range (0,len(stock)):
        strip_pairs = list()
        for inner_index in range (0, len(stock)):
            if(outer_index == inner_index):
                continue
            #If the strip we are testing matches better reversed, we will take that version
            normal_matches = find_matches(reverse_stock[inner_index],reverse_stock[outer_index])
            reverse_strip = reverse_stock[inner_index][::-1]
            reverse_matches = find_matches(reverse_stock[outer_index],reverse_strip)
            if reverse_matches > normal_matches:
                matches = tuple((reverse_strip,reverse_matches))
            else:
                matches = tuple((reverse_stock[inner_index], normal_matches))
            strip_pairs.append(matches)
        #Need to sort by the matches
        strip_pairs.sort(key= lambda x:x[1], reverse=True)
        key_value = list()
        for strip in strip_pairs:
            key_value.append(strip[0])
        strip_matches[reverse_stock[outer_index]] = key_value
    return strip_matches

def total_matches(carpet):
    """
    Finds the total number of matches within the carpet.
    ---
    PARAMS
    carpet : [String]
        the list of strips
    ---
    RETURN
    int
        returns the total number of matches between strips in the carpet
    """
    total_matches = 0
    for index in range (len(carpet)-1):
        total_matches += find_matches(carpet[index], carpet[index+1])
    return total_matches

def potential_matches(carpet, strip):
    """
    Computes the total number of matches our carpet would have if it included the given strip
    at the end.
    ---
    PARAMS
    carpet : [String]
        the list of strips representing the carpet
    strip : String
        the strip to potentially put at the end of the carpet
    ---
    RETURN
    int
        the total number of matches in the carpet if it had the given strip at the end
    """
    return total_matches(carpet) + find_matches(carpet[-1],strip)

def find_matches(strip_1, strip_2):
    """
    Finds the number of matches between two given strips.
    ---
    PARAMS
    strip_1 : String
        the first strip to compare
    strip_2 : String
        the second strip to compare
    ---
    RETURN
    int
        the total number of matches between the two given strips
    """
    matches = 0
    for index in range(len(strip_1)):
        if index >= len(strip_2):
            continue
        if strip_1[index] == strip_2[index]:
            matches = matches + 1
    return matches

if __name__ == '__main__':
    stock_list = ["RRR","BYB", "GGR", "RYL", "LLO", "ORR", "BRG", "BRR", "RYO"]
    found = compute_matches(stock_list)
    print(found)

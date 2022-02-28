__author__ = "Katelyn Harlan (4437710), Taya Nicholas (5926161), Samuel Terry (6786350)"

from collections import deque

def no_match_carpet(stock, length):
    """
    Simple depth first search implementation for a Carpet with no matches.
    ---
    PARAMS
    stock : [String]
        A list of strings representing strips in the stock
    length : int
        The desired size of the carpet, i.e. the number of strips needed for the final carpet
    ---
    RETURN
    String
        Either returns a no-match carpet, or if there is no such carpet returns "not possible"
    """

    stack = deque()
    for strip in stock:
        strips = []
        strips.append(strip)
        stack.append(strips)
    current_carpet = []
    finished = []

    while stack:
        current_carpet = stack.pop()
        children_list = get_children(current_carpet, stock)
        for child in children_list:
            stack.append(child)
        # if get_total_matches(current_carpet) == 0 and len(current_carpet) == length:
        #     finished = current_carpet
        #     break
        #For a child to be added to the stack, it must not have any matches, so we no longer need to check 
        #if the carpet has no total matches
        if len(current_carpet) == length:
            finished = current_carpet
            break
        current_carpet = []
    if(len(finished) == 0):
        return []
    return finished

def get_total_matches(carpet):
    """
    Returns the total number of matches within the carpet.
    ---
    PARAMS
    carpet : [String]
        a list of strings representing a carpet
    ---
    RETURN
    int
        The total number of matches in this carpet
    """
    total_matches = 0
    for index in range (len(carpet)-1):
        total_matches += find_matches(carpet[index], carpet[index+1])
    return total_matches

def find_matches(first_strip, second_strip):
    """
    Finds the number of matches between two strips.
    ---
    PARAMS
        first_strip: String
            the first strip to compare
        second_strip: String
            the second strip to compare
    ---
    RETURN
        int 
            the number of matches between the two strips
    """
    matches = 0
    for index in range(len(first_strip)):
        if index >= len(second_strip):
            continue
        if first_strip[index] == second_strip[index]:
            matches = matches + 1
    return matches


def get_children(current_carpet, stock):
    """
    Calculate all possible carpets that can be made by appending the strips in stock to this carpet
    Returns these children carpets as a list of Carpet objects
    ---
    PARAMS
    stock : [String]
        All strips given, including those already present in this carpet (these are filtered out before calculating children)
    ---
    RETURNS
    [String]
        A list of all possible carpets deriving from appending the stock strips to this carpet
    """

    #Make copy of stock and remove strips currently in carpet, also works for removing reversed strips
    temp_stock = stock.copy()
    for index in range (0, len(current_carpet) -1):
            strip = current_carpet[index]
            if strip in temp_stock:
                temp_stock.remove(strip)
            elif strip[::-1] in temp_stock:
                temp_stock.remove(strip[::-1])
    
    #Cycle through the remaining strips, checking against the end strip
    children_list = []
    end_strip = current_carpet[-1]
    for strip in temp_stock:
        if find_matches(end_strip, strip) == 0:
            child = current_carpet.copy()
            child.append(strip)
            children_list.append(child)
        if find_matches(end_strip, strip[::-1]) == 0:
            child = current_carpet.copy()
            child.append(strip[::-1])
            children_list.append(child)
    return children_list

if __name__ == '__main__':
    f = open("input/med_large.txt", "r", encoding="utf-16")
    contents = f.read()
    stock_list = contents.splitlines()
    f.close()
    print("Started")
    found = no_match_carpet(stock_list, 20)
    print(found)


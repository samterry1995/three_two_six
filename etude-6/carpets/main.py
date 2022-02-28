__author__ = "Katelyn Harlan (4437710), Taya Nicholas (5926161), Samuel Terry (6786350)"

from no_matches import no_match_carpet
from maximal import maximal_carpet
import sys

def main():      
    
    if len(sys.argv) != 3:
        print("Error: requires two arguments(carpet_size, carpet_type)")
        print(str(sys.argv))
        return

    carpet_size: int = int(sys.argv[1])
    carpet_type = sys.argv[2]
    stock = getinput()

    match carpet_type:
        case "-n":
            found = no_match_carpet(stock, carpet_size)
            if len(found) == 0:
                print("not possible")
            else:
                print(found)
        case "-m":
            if len(stock) < carpet_size:
                print("Error: carpet size cannot be larger than stock input")
                return
            (found, num_matches) = maximal_carpet(stock, carpet_size)
            print(found)
            print(num_matches)
        case "-b":
            print("Case balanced")
            print("Developing by other group member")

def getinput():
    result = list()
    for line in sys.stdin:
        result.append(line.rstrip())
    return result

if __name__ == "__main__":
    main()
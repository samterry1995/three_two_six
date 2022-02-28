import re
import sys

#A token contains a word if it starts with a whitspace or
#or A token also contains a word if it ends with punctuation, ", or whitespace.
#A word may start with a capital and may contain one apostrophe (not at the start).

def main():
    s = sys.stdout
    words =[]
    with open(sys.argv[1], 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            for word in line.split():
                if re.match(r'(^\"[A-Z]|^[A-Z]|^\"[a-z]|^[a-z])[a-z]*[\']?[a-z]*[!,.:;"?]?$',word):
                    if word[0] == '"':
                        word = word[1::]
                        words.append(word)
                    elif word[-1] == '!' or ',' or '.' or ':' or "'" or '"' or '?' or';':
                        word = word[:-1:]
                        words.append(word)                     
                    else:
                        words.append(word)
                    
    words.sort()
    j=0              
    for i in words:
        words[j] = words[j].lower()
        s.write(words[j]+'\n')
        j +=1
main()
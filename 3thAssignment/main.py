from math import log
from re import sub

# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
words = open("dictionary.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)

# Open input file and remove any mistaken spaces
input = open("file.txt","r").read().replace(" ","")

def add_spaces(s):
    # Find the best pair (match_cost, match_length) for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        ls = s.lower()
        return min((c + wordcost.get(ls[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))

# Add spaces between words
aux = add_spaces(input)
# Remove spaces before any of this -> . ? ! , : ;
aux2 = sub(r'\s([?.!,:;](?:\s|$))', r'\1', aux)
# Remove spaces after this " or ( and before " or )
output = sub(r'(["(])\s(.*)\s([")])', r'\1\2\3', aux2)

print(output)    
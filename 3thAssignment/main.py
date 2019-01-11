from math import log
import re
# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
words = open("dictionary.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)

def add_spaces(s):
    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
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

input = open("file.txt","r").read().replace(" ","")
output = re.sub(r'\s([?.!,:;](?:\s|$))', r'\1', add_spaces(input))
output = re.sub(r'(["(])\s(.*)\s([")])', r'\1\2\3', output)
print(output)    
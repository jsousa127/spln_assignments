from math import log
from re import sub
from sys import argv

words = open("dictionary.txt").read().split()

# Construir dicionario de custos - log do inverso da probabilidade(1/(i * log N))
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)

# Flag -i para dar o texto como input, ficheiro caso contrario
if argv[1] != "-i":
    input = sub(r'[\n\r\s]+',"",open(argv[1],"r").read())
else:
    input = argv[2]
    

def add_spaces(s):
    # Retorna o melhor par (custo, length) para os primeiros i caracteres
    def best_match(i):
        ls = s.lower()
        # Custos dos maxword indices a esquerda, comecando do vizinho
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        # Minimo custo para o seu indice somado ao custo da palavra que sobra caso exista
        return min((c + wordcost.get(ls[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Construir array de custos
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Identificar as palavras iterando a partir do ultimo caracter e escolhendo sempre a melhor palavra
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        out.append(s[i-k:i])
        i -= k
    # Acertar a pontuacao {.?!,:;(")}
    aux = sub(r'\s([?.!,:;](?:\s|$))', r'\1', " ".join(reversed(out)))
    aux2 = sub(r' - ',"-",aux)
    aux3 = sub(r'(["(\[])\s',r'\1', aux2)
    return sub(r'\s(["\])])', r'\1', aux3)
     


print add_spaces(input)
    

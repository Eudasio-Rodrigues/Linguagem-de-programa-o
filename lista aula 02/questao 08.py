#P = True e Q = False. Aplique De Morgan na seguinte proposição e 
#atribua o valor a uma variável - ~(p ^ (p v q)), 
# essa variável deve ser retornada partir de uma função

def De_Morgan(P, Q):
    proposicao = not(P or (P and Q))
    return proposicao
    
x=De_Morgan(True,False)
print(x)

#---// Criando o Tabuleito //----


tab = []

for i in range(0, 8):
    line = []
    for i in range(0,8):
        line.append("-")
    tab.append(line)
"""
for i in tab:
    print(i)
"""
#---// Resultado //----
"""
['-', '-', '-', '-', '-', '-', '-', '-']
['-', '-', '-', '-', '-', '-', '-', '-']
['-', '-', '-', '-', '-', '-', '-', '-']
['-', '-', '-', '-', '-', '-', '-', '-']
['-', '-', '-', '-', '-', '-', '-', '-']
['-', '-', '-', '-', '-', '-', '-', '-']
['-', '-', '-', '-', '-', '-', '-', '-']
['-', '-', '-', '-', '-', '-', '-', '-']
"""

#tab[0][0] = "&"
#tab[7][6] = "&" 

def check(i,j):
    atack = False 
    #Checking line
    for box in range(0, 8):
        if tab[i][box] == "&" and box != j:
            atack = True

    #Checking column
    for box in range(-2, 8):
        if tab[box][j] == "&" and box != i:
            atack = True
    
    #Checking Diagonal
    #Diagonal Positiva
    for ibox in range(0,8):
            try:
                if (i + ibox) != i and (j + ibox) != j:
                    if tab[i + ibox][j + ibox] == "&":
                        atack = True
            except:
                pass
    
    #Diagonal Negativa
    for ibox in range(0,8):
            try:
                if (i - ibox) >= 0 and (j - ibox) >= 0:
                    if (i - ibox) != i and (j - ibox) != j:
                        if tab[i - ibox][j - ibox] == "&":
                            atack = True 
            except:
                pass




    return atack
#########################################################
#---------// Solucao //----------------------








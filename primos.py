al = []


# Parte 1
def primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
            break
        elif i == num - 1:
            return True


# Parte 2
def proxprimo(r):
    n = r
    r = 1
    while True:
        r += 1
        if primo(r) == True:
            if r > n:
                break
            al.append(r)
    return al[0]


# Parte 3
def todosprimos(n):
    proxprimo(n)
    for i in list(al):
        print(i, end=" ")


# Executando programa final
todosprimos(int(input()))
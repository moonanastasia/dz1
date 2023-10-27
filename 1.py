def second(s):
    temp = "aeiou"
    summa_g = 0
    for i in temp:
        summa_g += s.lower().count(i)
    return summa_g

s = "Chocolate, tea and Coca-Cola have caffeine and they keep you awake. Try not to have them in the evening"
print(second(s))

def find_letter(strg, let):
    n = 0
    lst = []
    for i in range(len(strg)+1):
        x = strg[n:].find(let) + n
        lst.append(x)
        n = x + 1
    lst1 = list(set(lst))
    lst1.sort()
    print(lst1)
    return lst1

strg = input('Please insert your text: ')
lett = input('Please insert the letter you want to search for: ')
find_letter = find_letter(strg, lett)

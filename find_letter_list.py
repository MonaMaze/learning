
#Build your Function here 
def find_letter(strg, let):
    lst = []
    for a, b in enumerate(strg):
        if b == let:
            lst.append(a)
    print(lst)
    return lst
strg = input('Please insert your text: ')
lett = input('Please insert the letter you want to search for: ')
find_letter = find_letter(strg, lett)

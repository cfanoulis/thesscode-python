arr = [56, 200/9, 3]
arr.sort(reverse=True)
for num in arr:
    cmp = num*9
    if(cmp == 200):
        print('OK, it\'s 200. What did you expect me to say')
    elif(cmp > 200):
        print('Jesus christ. How the hell did you manage to get a number above 200')
    else:
        print('I didn\'t even ask for a high number. And you managed to give me a smaller one. Smaller than 200. SMFH')
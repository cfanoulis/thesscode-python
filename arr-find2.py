toFind = input('Enter the word you want to search for:\n')
src = input('Enter the text you want to search:\n')
srcArray = src.split(' ')
if toFind in src:
    print('Yes, the word', toFind, 'exists in your source text')
else:
    print('Sorry, I couldn\'t find the word you asked me to search :(')
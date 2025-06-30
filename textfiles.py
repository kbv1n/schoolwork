fileinput = str(input())

with open(f'{fileinput}', 'r+') as f:
    word1 = f.readline()
    word2 = f.readline()
    word3 = f.readline()
    sentence = ''.join(word1 + word2 + word3).replace('\n', ' ')
    f.write(f'\n{sentence}')

final = open(f'{fileinput}')
print(final.read())  


# with open('WordTextFile1.txt', 'a') as w:
#     w.write(sentence)


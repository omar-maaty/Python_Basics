fname=input('Enter the file path: ')
counts={}
try:
    with open(fname) as fopen:
        for line in fopen:
            words=line.split()
            for word in words:
                word=word.lower()
                counts[word]=counts.get(word,0)+1
    lst=[(v,k) for k,v in counts.items()]
    lst=sorted(lst,reverse=True)
    print('Top most frequent words:')
    x=1
    for (v,k) in lst[:5]:
        print(f'{x}.{k} ({v})')
        x +=1

except:
    print('File not founded')


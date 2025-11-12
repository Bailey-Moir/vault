#!/bin/python
import os
import matplotlib.pyplot as plt

VAULT = '~/Documents/vaults/vault/'
EXCLUDE = {
    '.git',
    '.trash',
    '.obsidian',
    'Assets',
    'Archive',
}
TABLE_SIZE = 2000 # A number >= your number of markdown tiles

table: list = [None] * TABLE_SIZE

def hashAdd(name: str, count: int):
    slot = hash(name)%TABLE_SIZE

    i = 0 # Number of iterations
    while table[slot] != None and table[slot][0] != name: 
        slot = (slot + 2*i + 1)%TABLE_SIZE # Quadratic by adding odd numbers
        i += 1

    if table[slot] == None:
        table[slot] = [name, count]
    else:
        table[slot][1] += count

def processMarkdown(directory: str):
    with open(os.path.expanduser(VAULT+directory), 'r') as source:
        content = source.read()
        count = 0

        for i in range(1,len(content),2):
            if content[i] != '[': continue

            # Make sure it's a link, and set i to the last '['
            if content[i-1] != '[':
                if content[i+1] == '[':
                    i += 1
                else:
                    continue

            # Account for '\[['
            if content[i-2] == '\\':
                if content[i+1] == '[':
                    i += 1
                else:
                    continue
            
            j = i + 1
            while content[j] not in ['|', '#', ']']: j += 1
            
            if j == i + 1: continue # [[#...]] means inner link

            hashAdd(content[i+1:j], 1)
            count += 1

        l,r = -1,-1
        for i in range(len(directory)-1,-1,-1):
            if directory[i] == '.':
                r = i
            elif directory[i] == '/':
                l = i + 1
                break

        hashAdd(directory[l:r], count)

def DFS(directory: str):
    if directory.endswith('.md'): # Leaf node
        processMarkdown(directory)
    elif '.' not in directory:
        for subitem in os.listdir(os.path.expanduser(VAULT+directory)):
            DFS(directory+'/'+subitem)

def tableCMP(tableEntry):
    if tableEntry != None:
        return tableEntry[1]
    else: return 0

for item in os.listdir(os.path.expanduser(VAULT)):
    if item not in EXCLUDE:
        DFS(item)

i = 1
for name, count in sorted(table, key=tableCMP, reverse=True)[:10]:
    print(f'{i}. {name} ({count})')
    i += 1

axes = plt.axes()

axes.hist([entry[1] for entry in table if entry != None], bins=range(max(table, key=tableCMP)[1]+1))

axes.grid(True)
axes.set_title("Degree Histogram :)")
axes.set_xlabel('Degree of note in graph')
axes.set_ylabel('Number of occurrences')
plt.show()

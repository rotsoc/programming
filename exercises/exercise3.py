from iteration_utilities import duplicates
from itertools import count


word_list = []
char_list = []
with open("wordlist.txt") as f:
    for line in f:
        word_list.append(line.replace("\n",""))
for word in word_list:
    char_list.append(sorted([char for char in word]))
dup = list(duplicates(char_list))
indices = []
for d in dup:
    indices.append([i for i, j in zip(count(), char_list) if j == d])
for ind in indices:
    for i in ind:
        print(word_list[i], end = ' ')
    



    

# Luke Scott
# COSC 311
# Lab 1
# Dr. Wang

import matplotlib.pyplot as plt

word_counts = {}
with open('SciencePaper.txt','r', errors='ignore') as file:
    for line in file:
        tokens = line.upper().replace(',','').replace(';','').replace('(','').replace(')','')\
        .replace('!','').replace('?','').replace('.','').split()
        for word in tokens:
            try:
                word_counts[word] += 1
            except:
                word_counts[word] = 1
                
word_lists = {}
for word,count in word_counts.items():
    try:
        word_lists[count].append(word)
    except:
        word_lists[count] = [word]
                
appearances = list(word_lists.keys())
num_words = [len(value) for value in word_lists.values()]
avg_len = [sum([len(word) for word in value]) / len(value) for value in word_lists.values()] 

total = sum(num_words)

print("Total number of words:", total)

print("The 10 words that appear most often are:")

sorted_by_count = sorted(word_lists.items())

count = -1
while count > -11:
    print(list(sorted_by_count)[count])
    count -= 1
    
print("\nAppearance Frequency of 'summerfelt' :",word_counts['SUMMERFELT'])
print("Appearance Frequency of 'wastewater' :",word_counts['WASTEWATER'])
print("Appearance Frequency of 'greenhouse' :",word_counts['GREENHOUSE'])
print("Appearance Frequency of 'salmon' :",word_counts['SALMON'])

#print("Words that appear once :\n",word_lists[1])
#print("Words that appear twice :\n",word_lists[2])
print("Words that appear 5 times :\n",word_lists[5])
print("Words that appear 10 times :\n",word_lists[10])

plt.bar(appearances, avg_len)
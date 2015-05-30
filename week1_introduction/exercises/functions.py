__author__ = 'Chris'

fruit = ['apple', 'orange', 'grape', 'kiwi', 'orange', 'apple']

# reports the frequency of every item

def analyze_list(l):

    counts = {}
    for item in l:
        if item not in counts:
            counts[item] = 0
        counts[item] += 1

    return counts

acounts = analyze_list(fruit)
print(acounts)

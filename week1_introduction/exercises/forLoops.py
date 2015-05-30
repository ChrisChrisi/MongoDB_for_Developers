__author__ = 'Chris'

fruit = ["apple", "orange", "grape"]

new_fruit = []

for item in fruit:
    print item

    new_fruit.append(item)

print new_fruit


person = {"name": "Chrisi", "age": "26", "location": "Sofia"}

for key in person:
    print "key is " + key + " value is " + person[key]

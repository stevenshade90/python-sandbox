numbers = list(range(1,101))
numbers.extend(numbers[::-1])

for num in numbers:
    print(num)

numbersToRemove = numbers[:]
numbersRemoved = []

while numbersToRemove:
    numbersRemoved.append(numbersToRemove.pop())

if len(numbersToRemove) == 0 and len(numbersRemoved) != 0:
    print("All numbers removed!")

print("Sorted numbersRemoved...")
numbersRemoved.sort()
for num in numbersRemoved:
    print(num)


removedDuplicates = list(set(numbersRemoved))
for num in removedDuplicates:
    print(num)

twoListsNested = [numbersRemoved[:], numbers[:]]

print(twoListsNested)

for num in twoListsNested:
    print(num)

for i in twoListsNested[0]:
    for j in twoListsNested[1]:
        print(i, j)
    print()

print(f'Index of 100: {removedDuplicates.index(100)}')
print(f'Number of 100 occurrances: {removedDuplicates.count(100)}')


print(102 in removedDuplicates)

for x in (sorted([1, 2, 3, 4, 5], reverse=True)):
    print(x, end=' ')
print()

y = [x for x in (sorted([1, 4, 2, 3, 5], reverse=True)) if x % 2 == 0]
print(y)

z = [x + y for x in "123" for y in "abc"]
print(z)

anotherWord = 'here'
unpackedList = [*'wordtounpack', *anotherWord, *range(0,100)]
print(unpackedList)

del unpackedList[:]
print(unpackedList)
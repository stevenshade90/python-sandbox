from methods import create_person as cp, read_person as rp

person_dictionaries = []

person_dictionaries.append(cp("Mark", "Matthews", 36, "SWE"))
person_dictionaries.append(cp("Jeremy", "Jones", 39, "IT"))
person_dictionaries.append(cp("Tom", "Garret", 41, "Tech"))


for person in person_dictionaries:
    rp(person)


print(person_dictionaries[0])
pop_val = person_dictionaries[0].pop('sshade', "No Value")

if pop_val:
    print(pop_val)

print(person_dictionaries[0].get('sshade', 'No Value for \'sshade\''))

for dictionary in person_dictionaries:
    print(dictionary)
    rp(dictionary)


print('zipping to a dictionary')
keys = ['steve', 'marty', 'ellen']
values = ['teacher', 'plumber', 'electrician']

D = dict(zip(keys, values))
print(f'Zipped dictionary -> {D}')
print('steve' in D)
print('frank' in D)

print(D.keys())
print(D.items())
DP = D.popitem()
print(f'DP values -> {DP}')

newDict = dict(name = DP[0], profession = DP[1])
print(newDict)

newDictKeys = newDict.keys()
print(newDictKeys)
for k, v in newDict.items():
    print(f'{k.title()}: {v.title()}')

dictUnpacked = {**D}
print(f'Unpacked dictionary -> {dictUnpacked}')

mergerDict = {'steve':'teacher', 'tim':'IT'}
print(mergerDict)
merged = D | mergerDict
print(f'Merging two dictionaries -> {merged}')


# dictComprehension = { x: x ** 2 for x in range(1,11) }
# print('All the powers of 2 for numbers 1-10')
# for k, v in dictComprehension.items():
#     print(f'\t{k}**2 = {v}')

mergerDict['steve'] = ['teacher', 'composer']
print(mergerDict)

mergerDict['steve'][0] = 'professor'
print(mergerDict)

print(mergerDict.get('jeremy', 'Name not found'))

ellenDictFromTuple = dict([DP])
print(ellenDictFromTuple)


D2 = dict(name= ([k for (k, v) in mergerDict.items() if 'professor' in v])[0])
print(D2)
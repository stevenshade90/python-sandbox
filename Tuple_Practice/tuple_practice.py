from collections import namedtuple

itemsList = ["Python", 3.14, False, None, "Hello"]
tupleMod = ((4,5) + (6,7))
tuple1 = (*itemsList, *(True, False), 5, *tupleMod, *['Goodbye', 'World'])

for item in tuple1:
    if type(item) == str:
        print(item)

tupleGenerator = tuple(x for x in range(10))
print(tupleGenerator)

print(tupleGenerator.index(5))
print(f'How many False values? => {tuple1.count(False)}')

Rec = namedtuple('Rec', field_names=['name', 'age', 'job', 'alive'])
person1 = Rec(name='John', age=20, job='Engineer', alive=True)
person2 = Rec(name='steve', age=20, job='SWE', alive=True)

print(person1)
print(person2)

person1AsDict = person1._asdict()
person2AsDict = person2._asdict()
print(person1AsDict)
print(person2AsDict)

unpackedPerson = [*person1AsDict.items()]
print(unpackedPerson)
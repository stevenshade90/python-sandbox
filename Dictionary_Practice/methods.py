def create_person(fname, lname, age, occupation):
    new_person = {}

    try:
        new_person[(fname[0]+lname).lower()] = {
            'first name' : fname,
            'last name' : lname,
            'age' : age,
            'occupation' : occupation
        }
    except Exception as e:
        print(e)

    return new_person


def read_person(dictionary):
    for username, internal_info in dictionary.items():
        print(username)
        print(f'First Name = {internal_info['first name']}')
        print(f'Last Name = {internal_info['last name']}')
        print(f'Age = {internal_info['age']}')
        print(f'Occupation = {internal_info['occupation']}')

        print()
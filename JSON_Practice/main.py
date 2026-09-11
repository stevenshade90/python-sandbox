import json

def Display(current):
    print(f'Name: {current["name"]}')
    print(f'\t=> Cores: {current["numberOfCores"]}')
    print(f'\t=> Memory: {current["memoryInMB"]} MB')
    print(f'\t=> OS Disk Size: {current["osDiskSizeInMB"]} MB')
    print(f'\t=> Resource Disk Size: {current["resourceDiskSizeInMB"]} MB')
    print(f'\t=> Available to use: {"Yes" if current["isAvailable"] == True else "No"}\n')


def DisplayAvailableSelections(selectionText):
    with open(selectionText, 'r') as f:
        data = json.load(f)
        data_dict = data['availableSizes']

        i = 0
        print(('*' * 4) + " Displaying Available Selections " + ('*' * 4))
        for item in data_dict:
            current_dict = data_dict[i]
            Display(current_dict)
            available.append(current_dict)

            i+= 1


def MatchingType(availableChoices, num):
    if num == 0:
        return

    for current in availableChoices:
        if current["numberOfCores"] >= num:
            Display(current)
            selection.append(current)


def SaveJson(filename, values):
    with open(filename, 'w') as f:
        json.dump(values, f, indent=4)

def LoadJson(filename):
    try:
        with open(filename) as f:
            if f:
                print("Found file!")

                data = json.load(f)
                if len(data) == 0:
                    print("No selections found!")
                    raise ValueError("No values are stored in the file")
                else:
                    print("Displaying your selections...")
                    for value in data:
                        Display(value)
    except FileNotFoundError as e:
        print(f'Error loading file: {e}')
    except ValueError as e:
        print(f'Error loading values: {e}')


if __name__ == '__main__':
    available = []
    selection = []

    saveFileJson = 'saved_choice.json'
    availableSelections = 'available_selections.txt'

    LoadJson(saveFileJson)
    DisplayAvailableSelections(availableSelections)
    cores = input('How many cores do you need: ')
    MatchingType(available, int(cores))
    SaveJson(saveFileJson, selection)
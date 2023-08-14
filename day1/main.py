
'''
Returning a list of tuples.
[(x, y)...]
x -> elf number
y ->  total calories
'''
def getListOfElfs():
    with open('adventofcode.com_2022_day_1_input.txt', 'r') as file:
        elfs = []
        numElfs = 0
        totalCal = 0
        for i in file.readlines():
            if i == "\n":
                numElfs +=1
                elfs.append((numElfs, totalCal))
                totalCal = 0
            
            if i != "\n":
                totalCal += int(i.strip('\n'))
    return sorted(elfs, key=lambda x: x[1], reverse=True)


'''
Returning a tuple containing the elf number and it's total calories
'''
def maxCalories():
    return getListOfElfs()[0]


    


if __name__ == "__main__":
    elfNum, totalCal = maxCalories()
    print("Elf number {} is the maximum carrier of a total of {} calories.".format(elfNum, totalCal))
    # print(getListOfElfs())
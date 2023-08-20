def getInputs() -> tuple[list, list]:
    crates = []
    instructions = []
    with open('adventofcode.com_2022_day_5_input.txt', 'r') as file:
        newLine = False
        for i in file.readlines():
                if newLine == False:
                    crates.append(i.strip('\n').split(' '))
                    if i == '\n':
                        newLine = True
                        crates.pop()
                else:
                    instructions.append(i.strip('\n'))
        
    return rotateCrate(crates), instructions

def cratify(crates):
    newCrate = []
    row = 0
    numSpaces = 0
    for i in range(len(crates)):
        newCrate.append([])
    
    for crate in crates:
        for item in crate:
            if item == '' and numSpaces >= 3:
                newCrate[row].append('')
                numSpaces = 0
            elif item != '':
                newCrate[row].append(item)
            else:
                numSpaces += 1
        row += 1
    newCrate.pop()
    return newCrate

def reverseCrateItems(crates):
    newCrate = []
    for i in range(len(crates)):
        newCrate.append([])
        for j in range(len(crates[i]), 0, -1):

            newCrate[i].append(crates[i][j-1])
    return newCrate

def rotateCrate(crates):
    newCrate = []
    cratified = cratify(crates)
    row = 0
    
    for i in range(len(cratified)):
        newCrate.append([])
        
    for crate in cratified:
        for item in crate:
            if item == '':
                row += 1
            else:
                newCrate[row].append(item)
                row += 1
        row = 0
    return reverseCrateItems(newCrate)

def printSteps(crates):
    containerNum = 1
    for crate in crates:
        print(containerNum, end=' ')
        for item in crate:
            print(item, end='')
        print()
        containerNum += 1
    print()
                
# Part 1
def solve():
    crates, instructions = getInputs()
    
    for instruction in instructions:
        decryptInst = instruction.split(' ')
        decryptInst.remove('move')
        decryptInst.remove('from')
        decryptInst.remove('to')
        quantity, fromPos, toPos = map(int, decryptInst)
        
        for i in range(quantity):
            take = crates[fromPos-1].pop()
            crates[toPos-1].append(take)
            printSteps(crates)
    
    
        
        
if __name__ == "__main__":
    print(solve())
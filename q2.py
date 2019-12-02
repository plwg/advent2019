import os, math, copy

def main():
    file = open('q2_input.txt')
    opCode = file.read().split(',')
    opCode = list(map(int, opCode))
    goalSeek(opCode, 19690720)

def execute(opCode, head):

    if opCode[head] == 1:
        opCode[opCode[head+3]] = opCode[opCode[head+1]] + opCode[opCode[head+2]]
        execute(opCode, head + 4)
    elif opCode[head] == 2:
        opCode[opCode[head+3]] = opCode[opCode[head+1]] * opCode[opCode[head+2]]
        execute(opCode, head + 4)
    else:
        return None

def goalSeek(opCode, goal):

    for i in range(100):
        for j in range(100):
            newopCode = generateNewOpCode(opCode, i, j)
            execute(newopCode,0)
            if newopCode[0] == goal:
                print('Code is %s.' % (i * 100 + j))

def generateNewOpCode(origin, noun, verb):

    newopCode = copy.deepcopy(origin)
    newopCode[1] = noun
    newopCode[2] = verb

    return newopCode
    

if __name__ == '__main__':
    main()

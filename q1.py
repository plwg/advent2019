import os, math

def main():
    file = open('q1_input.txt')
    listModule = file.read().split()
    smartTotalFuel(listModule)

def simpleFuel(modules):
    fuel = 0
    for module in modules:
        fuel += math.floor(int(module)/3) - 2
    print(fuel)
    return None

def smartTotalFuel(modules):
    totalFuel = 0
    for module in modules:
        totalFuel += smartSingleFuel(module)
    print (totalFuel)
    return None

def smartSingleFuel(module):

    requiredFuel = math.floor(int(module)/3) - 2

    if requiredFuel < 0:
        requiredFuel = 0
    else:
        requiredFuel += smartSingleFuel(requiredFuel)
    return requiredFuel
    
if __name__ == '__main__':
    main()
    
    


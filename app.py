def average(nummers: []) -> float:
    sum = 0
    for number in nummers:
        sum += number
    return sum / len(nummers)


def greatest(numbers: []) -> int:
    cool = 0
    for number in numbers:
        if number > cool:
            cool = number



if __name__ == '__main__':
    print ('hbjdfgvjsd')
    nummers = [0,1,2,3,4]
    print (average(nummers))

    numbers = [512761284]
    print (greatest (nummers))


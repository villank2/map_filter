#map and filter functions


def map_filter():
    numbers = [1,2,3,4,5]

    powers_of_two = map(lambda x: x**2,numbers)

    for number in filter(lambda x: x<20,powers_of_two):
        print(number)

def type2():
    numbers = [1,2,3,4]

    powers = (2**x for x in numbers)
    for x in powers:
        print(x)
    for n in (x**2 for x in powers if x < 20):
        print(n)

if __name__ == '__main__':
    type2()
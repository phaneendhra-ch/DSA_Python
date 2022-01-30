"""

Number Factor in Python

Find Combinations of a number as a sum of 1,3,4

    Formula:
    NumberFactor(n) = NumberFactor(n-1) + NumberFactor(n-3) + NumberFactor(n-4)

    Eg : 5
    Total no.of ways = 6
    (4,1) (1,4) (3,1,1) (1,1,3) (1,3,1) (1,1,1,1,1)

"""

def number_factor(number : int ):

    if number in [0,1,2]:
        return 1

    elif number == 3:
        return 2
    else:
        part1 = number_factor(number-1)
        part2 = number_factor(number-3)
        part3 = number_factor(number-4)

        print(f"part1 : {part1} part2 : {part2} part3 : {part3}")
        return part1 + part2 + part3

if __name__ == '__main__':
    number  = int(input("Enter a number : "))
    print(f"Number Factor for {number} is : {number_factor(number)}")


def collatz(number):
    int(number)
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1
number = input()
int(number)
collatz(number)
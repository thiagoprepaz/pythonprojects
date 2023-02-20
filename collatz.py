
def collatz(number):

    if number % 2 == 0:
        return(print(number // 2))
        
    else:
        return(print(3 * number + 1))
number = input()
collatz(int(number)) 
number = input()

def collatz(number):

        if number % 2 == 0:  # if the rest of the division is equal to 0 it's a even number
            ver = number // 2
            print(number // 2)
            verification(int(ver))

        else:  # if that's not a even, it only can be a odd
            ver = 3 * number + 1
            print(3 * number + 1)
            verification(int(ver))

def verification(ver):
        if ver != 1:
            collatz(number)
        else:
            return(print("You are done"))
collatz(int(number))
   
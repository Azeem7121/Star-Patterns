"""
Write a programme in which you will take input from user and return a pattern of star(*)
first input number of rows or number between 1-50
second input number 0 or 1 and typecast to boolean which sats 1 = true and 0 = false
now return pattern
if true and number is 5 returns this
    *
    **
    ***
    ****
    *****
if false and number is 5 returns this
    *****
    ****
    ***
    **
    *

"""


# Pattern programme

class Pattern:
    @staticmethod
    def forward_pattern():
        for i in range(1, n + 1):
            print(" * " * i, end="")
            print("\r")

    @staticmethod
    def reverse_pattern():

        for i in range(n, 0, -1):
            print(" * " * i, end="")
            print("\r")


while 1:
    c = Pattern()
    print("""
    To Continue press-[ENTER]
    
    To Quit press-[Q] and Enter
    """)
    a = input(":- ")
    a = a.upper()
    if a == "Q":
        break
    else:
        print("Enter any number between 1 - 50")
        n = int(input())
    if n < 1:
        print("!!!please enter the number between the given range!!!")
        print()
        continue
    if n > 50:
        print("!!!please enter the number between the given range!!!")
        print()
        continue
    print()
    print("Enter a number 0 or 1")
    b = int(input())
    if bool(b) is True:
        c.forward_pattern()
        print()
        print("Great!")
        print()

    elif bool(b) is False:
        c.reverse_pattern()
        print()
        print("Great!")
        print()

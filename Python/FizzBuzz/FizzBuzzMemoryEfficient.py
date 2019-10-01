fizzer = []

r: int = 10000
fizz: int = 3
buzz: int = 5

for x in range(1,r,1):

    if x % fizz == 0 and x % buzz == 0:
        fizzer.append("FizzBuzz")
    elif x % fizz == 0:
        fizzer.append("Fizz")
    elif x % buzz == 0:
        fizzer.append("Buzz")
    else:
        fizzer.append(x)

print(fizzer)

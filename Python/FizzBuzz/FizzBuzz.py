fizzer = []

r: int = 10000
fizz: int = 3
buzz: int = 5

for x in range(r):

    tmp = ""
    
    if (x % fizz == 0) and (x != 0):
        tmp = tmp + "Fizz"
        
    if (x % buzz == 0) and (x != 0):
        tmp = tmp + "Buzz"
        
    if tmp == "":
        tmp = x
        
    fizzer.append(tmp)

print(fizzer)

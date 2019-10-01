# FizzBuzz

### Overview

Brief history of FizzBuzz can be found [here](https://en.wikipedia.org/wiki/Fizz_buzz)

### Design / Architecture

Fizzbuzz is a rather simple but apparently constant thorn in the side of newer programmers that lack actual experience in writing implementations.
This quick-write allows more configuration of FizzBuzz (though to be totally honest not sure why you would but whatever!)

```
fizzer = []

r: int = 10000
fizz: int = 3
buzz: int = 5
```

Parameters of the game: A list to hold values that we'll echo at the end, the range to iterate over, and the configuration of Fizz and Buzz divisors.

```
for x in range(r):
    tmp = ""
    if (x % fizz == 0) and (x != 0):
        tmp = tmp + "Fizz"
    if (x % buzz == 0) and (x != 0):
        tmp = tmp + "Buzz"
    if tmp == "":
        tmp = x
    fizzer.append(tmp) 
```

In this case since we're iterating through a range with complexity O(n) we can use two implementations of the range() function:

```
range(r)
```

Will simply start us at 0 and go to the iteration ending non-inclusively (note the output will end at 9999 as 0 - 9999 is 10k iterations

If we use range(r) implementation we will need to check for (x != 0) as in modulo evaluations 0 % num == 0

```
range(1, r)
```

However if we perform this implementation of range() we will go from 1 - 10k iterations and won't require the (x != 0) check because, well, we didn't start at 0. Pretty self explanatory there.

```
tmp = ""
```

We can be a bit more relaxed approaching FizzBuzz this way as all we're really doing is string concatenation. This will unfortunately use more memory (though come on it's not like it's that much) due to strings being created multiple times.

```
print(fizzer)
```

Self explanatory, we echo out the list of the collection results. Ta-Da!


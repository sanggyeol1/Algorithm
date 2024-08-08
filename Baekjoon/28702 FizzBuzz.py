a = input()
b = input()
c = input()

if a != "Fizz" and a != "Buzz" and a != "FizzBuzz":
    a = int(a)
    i = a+3

elif b != "Fizz" and b != "Buzz" and b != "FizzBuzz":
    b = int(b)
    i = b+2


elif c != "Fizz" and c != "Buzz" and c != "FizzBuzz":
    c = int(c)
    i = c+1


if i % 3 == 0 and i % 5 != 0:
    print("Fizz")
elif i % 3 != 0 and i % 5 == 0:
    print("Buzz")
elif i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz") 
else:
    print(i)
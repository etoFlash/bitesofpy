def fizzbuzz(num):
    result = ""
    if not num % 3:
        result = "Fizz"
    if not num % 5:
        result = "Buzz" if not result else result + " Buzz"
    return num if not result else result

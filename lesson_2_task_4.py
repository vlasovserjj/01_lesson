def fizz_buzz(n):
    for n in range(1, n):
        thr = (n % 3 == 0)
        fv = (n % 5 ==0)
        if thr:
            print("Fizz")
        if fv:
            print("Buzz")
        if thr and fv:
            print("FizzBuzz")
        print(n)
fizz_buzz(17)

from test_utils import test_sort
def fib1(n):
   if n <= 1:
       return n
   lst = [0] * (n + 1)
   lst[1] = 1
   for i in range(2, n + 1):
       lst[i] = lst[i - 1] + lst[i - 2]
   return lst[n]


test_sort(fib1(13))

assert fib1(7) == 13


def fib2(n):
    if n <= 1:
        return n
    res = fib2(n-1)+fib2(n-2)
    return res


assert fib2(7) == 13

# for i in range(100):
#    print(f'{i}th number (fib1): {fib1(i)}')
#    print(f'{i}th number (fib2): {fib2(i)}')

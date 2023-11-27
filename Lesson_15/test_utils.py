import random
import copy


def generate_list(n: int):
   return [random.randint(0, n ** 2) for _ in range(n)]


def test_case(sort_func: callable, n: int):
   lst = generate_list(n)
   copy_lst = copy.deepcopy(lst)
   sorted_lst = sort_func(lst)
   assert lst == copy_lst, 'Sort function must not change the original list'
   assert len(sorted_lst) == n
   assert all(sorted_lst[i] <= sorted_lst[i + 1]
              for i in range(len(sorted_lst) - 1)), \
       'List is not sorted'


def test_sort(sort_func: callable):
   test_case(sort_func, 0)
   test_case(sort_func, 1)
   test_case(sort_func, 2)
   test_case(sort_func, 10)
   test_case(sort_func, 100)
   test_case(sort_func, 1000)
   test_case(sort_func, 10000)


if __name__ == '__main__':
   test_sort(lambda x: list(sorted(x)))

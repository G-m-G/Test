def cache(func):
  cache_dict = dict()
  def wrapper(num):
    if num in cache_dict:
      return cache_dict[num]
    else:
      cache_dict[num] = func(num)
      return cache_dict[num]
  return wrapper

@cache
def fib_num(num):
  if num <= 2:
    return 1
  return fib_num(num-2) + fib_num(num-1)

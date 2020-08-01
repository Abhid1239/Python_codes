print((lambda x,y: x**2 - y**2 +4*x*y)(-4, -5))
#to use lambda instead of defining the whole variable

def my_func(f, arg):
  return f(arg)


my_func(lambda x: 2*x*x, 5)


def add_5(x):
  return round(x*100 , 2)

nums = [1,2,3,4,54,67,434,534,6,6545.53,553.4246543]
result = list(map(add_5, nums))
#mapping to map every variable from list and perform any operations into it
print(result, "this is it")
result = list(map(lambda x: round(x*100, 3), nums))
print(result)


res= list(filter(lambda x: x%2!=0, nums))
print(res)
#filter to filter any function if doesnt staisfy the equation


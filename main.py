# Implement all functions below

def separate_even_odd(numbers):
    even = []
    odd = []
    for n in numbers:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    return even, odd
print(separate_even_odd([1,2,3,4]))



def flatten_once(nested_list):
    result = []
    for sublist in nested_list:
        result.extend(sublist)
    return result
print(flatten_once([[1,2],[3,[4]]]))

def index_map(items):
    map = {}
    for i,item in enumerate(items):
        map[item] = i
    return map
print(index_map(['a','b','c']))
    


def lowest_value_key(data):
    new = min(data,key = data.get)
    return new
print(lowest_value_key({'a':5,'b':2,'c':3}))


def sort_by_last_letter(words):
    return sorted(words, key=lambda x: (x[-1], x))
print(sort_by_last_letter(["cat","dog","bat"]))



def categorize_products(products):
    cart = {}
    for product in products:
        name = product["name"]
        category = product["category"]
        if category not in cart:
            cart[category] = []
        cart[category].append(name)
    return cart
print(categorize_products([
            {"name":"Milk","category":"Dairy"},
            {"name":"Cheese","category":"Dairy"},
            {"name":"Apple","category":"Fruit"}
        ]))

def reverse_dict(data):
    return {v: k for k, v in data.items()}
print(reverse_dict({'a':1,'b':2}))


def shift_left(nums, k):
    k = k % len(nums)  
    return nums[k:] + nums[:k]
print(shift_left([1,2,3,4],1))


def sort_by_username(emails):
    return sorted(emails, key=lambda x: x.split("@")[0])
print(sort_by_username(["bob@gmail.com","alice@yahoo.com"]))


def has_common_elements(list_a, list_b):
    return any(item in list_b for item in list_a)
print(has_common_elements([1,4],[3,2]))


def safe_get(data, key):
    return data.get(key, "Missing")
print(safe_get({'a':1},'a'))
print(safe_get({'a':1},'b'))


def cumulative_sum(n):
    return sum(range(1, n + 1))
print(cumulative_sum(5))


def custom_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]

    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib
print(custom_fibonacci(5))
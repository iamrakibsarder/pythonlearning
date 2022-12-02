from htmlTag import getTag as tag

def sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total


result = sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

print(tag('Hey Rakib Bhai', 'p'))

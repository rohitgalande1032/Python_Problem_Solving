# swap two numbers without using third variable

def swap(x, y):
    # x = 3, y = 2
    x = x + y # x = 5
    y = x - y # y = 5-2 = 3
    x = x - y # x = 5-3 = 2

    return x, y  #swapped
x = 2
y = 3

print(f"After swapping:(x, y) = {swap(x, y)}")
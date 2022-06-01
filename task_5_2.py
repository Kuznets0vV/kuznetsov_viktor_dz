
def gen(num):
    return (nums for nums in range(0, num) if nums % 2 != 0)


for i in gen(10):
    print(i)

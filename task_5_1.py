

def gen(num):
    for nums in range(0, num):
        if nums % 2 != 0:
            yield print(nums)


generator = list(gen(15))



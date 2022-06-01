import time

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

start = time.perf_counter()
result = []
[result.append(i) for i in src if src.count(i) == 1] # медленный вариант
end = time.perf_counter()
print(result, f'время исполнения {end - start} s')

start = time.perf_counter()
res = set()
tmp = set()
for el in src:
    if el not in tmp:
        res.add(el)
    else:
        res.discard(el)
    tmp.add(el)
result_opti = [el for el in src if el in res] # быстрый вариант
end = time.perf_counter()
print(result_opti, f'время исполнения {end - start} s')

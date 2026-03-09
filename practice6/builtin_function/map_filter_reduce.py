n=int(input())
m=list(map(int, input().split()))
res=list(map(lambda x:x**2, m))
print(sum(res))


words = ["apple", "banana"]
print(list(map(str.upper, words)))


n=int(input())
m=list(map(int, input().split()))
res=list(filter(lambda x:x%2==0, m))
print(len(res))


words = ["cat", "lion", "dog", "tiger"]
long_words = list(filter(lambda w: len(w) > 3, words))
print(long_words)


from functools import reduce
nums = [1, 2, 3, 4, 5]
# lambda acc, x: acc + x → добавляем каждый элемент к аккумулятору
total = reduce(lambda acc, x: acc + x, nums, 0)
print(total)

product = reduce(lambda acc, x: acc * x, nums, 1)
print(product)
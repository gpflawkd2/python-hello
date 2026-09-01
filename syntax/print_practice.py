# 3가지 format practice
x = 50
y = 100
text = 30143458904
n = 'Lee'

# 예제_1
ex1 = 'n = %s, s = %s, sum = %d' % (n, text, (x+y))
print(ex1)

# 예제_2
ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n=n, s=text, sum=(x+y))
print(ex2)

# 예제_3
ex3 = f'n = {n}, s = {text}, sum = {x+y}'
print(ex3)
print(f'n = {n}, s = {text}, sum = {x+y}')

# 구분기호
m = 1000000000
print(f'm = {m:,}') # 1,000,000,000

# 정렬
# ^ : 가운데, < : 왼쪽, > : 오른쪽

t = 20
print(f"t : {t:10}")
print(f"t center : {t:^10}")
print(f"t : {t:<10}")

print(f"t center : {t:*^10}")
print(f"t : {t:#<10}")
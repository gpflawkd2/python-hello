# 숫자형 연산자

"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) : x의 y제곱 = x ** y
"""

# 형 변환 예제
a = 3.
b = 6
c = .7
d = 12.7

print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True = 1
print(float(False)) # False = 0.0
print(complex(a)) # complex(3.0, 0.0)
print(complex('3')) # 문자형 -> 숫자형

# 수치 연산 함수
print(abs(-7))

x, y = divmod(100, 8) # 몫과 나머지
print(x, y)
print(divmod(100, 8))

print(pow(5, 3), 5 ** 3)

# 외부 모듈
import math

print(math.pi)
print(math.ceil(5.1)) # 올림
print(math.floor(5.9)) # 내림
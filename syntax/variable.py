# 변수

# 기본선언
n = 700

print(type(n))

# 동시선언
x = y = z = 700
print(x, y, z)

var = 75
var = "change value"

print(type(var))
print(var, type(var))

# id(identity) 확인 : 객체의 고유값 확인

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n)) # False

# 동일한 값의 변수는 동일한 객체를 참조한다.
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n)) # True

# 다양한 변수 선언
# Camel Case : myVariableName -> Method
# Pascal Case : MyVariableName -> Class
# Snake Case : my_variable_name -> Variable

# 예약어는 변수명으로 불가능
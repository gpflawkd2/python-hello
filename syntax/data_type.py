# data type

"""
int : 정수
float : 실수
complex : 복소수
bool : 불리언(True, False)
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전(키, 값)
"""

str1 = "Python"
str2 = "Programming"

list = [str1, str2]
dict = {
    "name" : "Machine Learning",
    "Version" : 2.0
}
tuple = (7, 8, 9)
set = {3, 5, 7}

# 데이터 타입 출력
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))
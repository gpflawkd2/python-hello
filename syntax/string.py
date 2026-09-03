# 문자형

str1 = "I am Python"
str2 = "Python"
str3 = """How are you?"""
str4 = '''Thank you!'''

print(len(str1)) # 문자열 길이(공백포함)

# 빈 문자열
str_t1 = ''
str_t2 = str()

# 이스케이스 문자 사용
print("I'm Boy")
print('I\'m Boy')

print('a \t b') # 탭 문자
print('a \n b') # 줄바꿈 문자

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# Raw String : Escape 문자 처리하지 않음
raw_s1 = r'D:\python\test'
print(raw_s1)

# 멀티라인 입력
# 역슬래시(\) 사용
multi_str1 = """
스트링
멀티라인
테스트
"""

multi_str2 = \
'''
String
Multi line
Test
'''

multi_str3 = \
'String ' \
'Multi line ' \
'Test'\

print(multi_str1)
print(multi_str2)
print(multi_str3)

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing?"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3) # 문자열 반복
print(str_o1 + str_o2) # 문자열 연결

# 시퀀스는 in 연산 가능
print('y' in str_o1) # 포함 관계 확인 : True
print('P' not in str_o2) # 포함 관계 확인 : True

# 문자열 형뱐환
print(str(66), type(str(66))) # 정수 -> 문자열
print(str(10.1), type(str(10.1))) # 실수 -> 문자열
print(str(True), type(str(True))) # 불리언 -> 문자열


# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)

print("Capitalize: ", str_o1.capitalize()) # 첫 글자만 대문자로 변경
print("end with 's': ", str_o2.endswith('s')) # 문자열 끝 확인
print("replace: ", str_o1.replace('thon', ' Good')) # 문자열 변경
print("sorted: ", sorted(str_o1)) # 문자열 정렬 후 리스트 반환
print("split: ", str_o4.split(' ')) # 문자열 분리 후 리스트 반환

# 반복(시퀀스)
im_str = "Good Boy!"

# 문자열 관련 함수 목록 출력
# ___iter___ : 반복 가능한 객체인지 확인
print(dir(im_str))

for i in im_str:
    print(i)
    
# 슬라이싱
# 양수는 왼쪽에서 오른쪽으로, 음수는 오른쪽에서 왼쪽으로
# 3번째 변수는 step으로 건너뛰는 간격을 의미함
str_sl = "Nice Python"

print(str_sl[0:3]) # 0~2까지(0부터 3번째 전까지)
print(str_sl[5:11]) # 5~10까지(5부터 11번째 전까지)
print(str_sl[5:]) # 5~끝까지
print(str_sl[:len(str_sl)]) # 처음부터 끝까지
print(str_sl[1:9:2]) # 1~8까지 2칸씩 건너뛰기 : iePt
print(str_sl[-5:]) # 뒤에서 5번째부터 끝까지
print(str_sl[1:-2]) # 1~뒤에서 3번째까지 : ice Pyth
print(str_sl[::2]) # 처음부터 끝까지 2칸씩 건너뛰기 : Nc yhn
print(str_sl[::-1]) # 처음부터 끝까지 역순 : nohtyP eciN

# 아스키 코드(또는 유니코드)

print(ord('z')) # 아스키 코드로
print(chr(122)) # 문자로
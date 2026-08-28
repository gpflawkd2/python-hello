# print 사용법


# 기본 출력
print('Python Start!') 
print("Python Start!") 
print("""Python Start!""")
print('''Python Start!''')

#separator 옵션 : 구분자로 문자를 결합
print('P', 'Y', 'T', 'H', 'O', 'N',sep='|')
print('010', '1234', '5678', sep='-')
print('python', 'google', 'naver', sep='@') 

#end 옵션 : 출력 후 끝 문자를 지정
print('Welcome To', end='^')
print('IT News Web Site', end='\n')

#file 옵션 : 출력 내용을 파일로 저장
import sys

print('Learn Python', file=sys.stdout)
print()

#format 옵션 : 문자열 포맷팅(d, s, f)

# %s : 문자열
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two')) # 인덱스 지정 가능

print('%10s' % ('nice')) # 10칸 확보 후 오른쪽 정렬, 숫자는 자릿수를 의미함
print('{:>10}'.format('nice')) # 10칸 확보 후 오른쪽 정렬
print('{:_>10}'.format('nice')) # 10칸 확보 후 오른쪽 정렬, 빈칸을 '_'로 채움

print('%-10s' % ('nice')) # 10칸 확보 후 왼쪽 정렬
print('{:<10}'.format('nice')) # 10칸 확보 후 왼쪽 정렬

print('{:^10}'.format('nice')) # 10칸 확보 후 가운데 정렬
print('%.5s' % ('pythonstudy')) # 5칸 확보, .을 붙여야 문자열 자릿수 제한
print('{:10.5}'.format('pythonstudy')) # 10칸 확보 후 5칸만 출력
print()

# %d : 정수형
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42)) 
print('{:4d}'.format(42)) # 정수일 때는 parameter에 d를 붙여야 함
print()

# %f : 실수형
print('%f' % (3.141592653589793))
print('{:f}'.format(3.141592653589793))
print('%06.2f' % (3.141592653589793))   # 6칸 확보, 소수점 2자리까지 표시, 빈칸은 0으로 채움
print('{:06.2f}'.format(3.141592653589793))
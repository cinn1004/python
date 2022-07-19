python = "Python is Amazing"
print(python.lower()) #다 줄이기
print(python.upper()) #다 대문자
print(python[0].isupper()) # 이거 대문자 맞니 ??
print(len(python))
print(python.replace("Python","Java"))

# 특정문자가 첫번째로 나온 인덱스 값.
index = python.index("n")
print(index)

# 특정문자가 두번째로 나온 인덱스 값.
index = python.index("n",index+1) ## n 이 두번째로 나온 경우.
print(index)

# find 함수
print(python.find('java')) # -> 없으면 -1
# index 함수
print(python.index("java")) # -> index는 오류가 남.
# count 함수
print(python.count("n"))

'''
lower 소문자
upper 대문자
isupper 이거 대문자 맞아 ?
spring.replace(A,B) spring내의 A를 B로 바꾸기
index(a) -> 제일 처음으로 a라는 문자열이 나온 인덱스  
'''

#d
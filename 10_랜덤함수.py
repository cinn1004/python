from random import * # random import 필요함 !!!

# random() 0에서 1미만의 임의의 값을 생성
print(random()) # 0에서 1미만의 임의의 값
print(random()*10) # 0에서 10미만의 임의의 값 
print(int(random()*10)) # 0에서 10미만의 임의의 정수 값 
# random() 을 활용
print(int(random()*10)+1) # 0에서 10 이하의 임의의 정수 값 
print(int(random()*45)+1) # 0에서 45 이하의 임의의 정수 값 


# 편하게 할수있는거 / 미만 버전
print(randrange(1,46)) # 1부터 46 미만의 임의의값 생성

# randint 편하게 할수있는거 2 / 이하 버전
print(randint(1, 45)) # 1~45 이하의 임의의 값 생성
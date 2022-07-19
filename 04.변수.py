# 변수 : 값을 저장하는 공간 
name = '리온이'
animal = '강아지'
age = 4
hobby = "산책"
is_adult = age >=3 # 3살이상이면어른이다.

print("우리집 "+animal+"의 이름은 "+name+"이에요.")
# 이렇게 다 쉼표로 할 경우 모두 모두 띄어쓰기가 된다.
print(name,"은 ",age, "살이며, ","산책을 아주 좋아해요." )
# age의 경우 한칸 띄워지기 때문에 str(변수)의 형태로 넣는것이 좋다.
print(name+"은 ",str(age)+"살이며,",hobby+"을 아주 좋아해요." ) 
# 문자열끼리는 더하기가 그냥 가능하지만, 정수와 문자열 or 불리언과 문자열의 더하기는 불가능하다.
print(age+"살이며")
print(name+"는 어른일까요?"+str(is_adult))
# 슬라이싱은 리스트에서도 나오니 항상~ 기억하기

jumin = "010403-2234567"

print("성별 : "+jumin[7])
print("연 : "+jumin[:2])
print("월 : "+jumin[2:4])
print("일 : "+jumin[4:6])

print("생년월일 :"+jumin[0:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:] )


# 맨뒤에서부터 7번째에서 가져오기
print("뒤 7자리 : " + jumin[-7:] )
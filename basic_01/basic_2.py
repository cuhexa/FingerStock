#2.3 제어문
#
# stock_name = "삼성전자"
# if stock_name == "삼성전자":
#     print("pass")

# stock_price = 3000
# if stock_price > 3000:
#     print("pass1")
# elif stock_price == 3000:
#     print("pass2")
# elif stock_price < 3000:
#     print("pass3")
# else:
#     print("no applicable")

# stock_price = 2000
# if stock_price < 3000 or stock_price >= 3000:
#     print("anything")

# stock_price = 3000
# if stock_price > 2000 and stock_price < 2500:
#     print("2000~2500사이")
# elif stock_price >= 2500 and stock_price <= 3000:
#     print("2500~3000사이")
# else:
#     print("기준 구간을 벗어납니다.")


# 2.3.2 for 반복문
# for i in range (5,100):
#     print(i)
#     if i == 50:
#         break


#for 문 안에 for 문을 넣기
# for i in range (0,10):
#     for k in range (0,5):
#         print("for 문 안에 for 문 %s" % k)

# 2.3.3 while 반복문
# stock_buy = True
# count = 0
# while stock_buy:
#     count = count + 1
#
#     if count == 10:
#         #break
#         stock_buy = False
#
#     print(count)

#2.3.4 연습문제
# 문제3) 3일 후의 주가 비교하기
# 카카오증권의 현재가는 1000원이며, 3일 동안 500원씩 연달아 올랐다.
# 키움증권의 현재가는 500원이며, 3일 동안 1000원씩 연달아 올랐다.
# 3일 후의 현재가는 누가 더 높은가?
# 출력문구 : 키움이 더 놓다.
# 문제4) 구구단 출력하기
# 다음과 같은 형식으로 구구단을 출력하라(30분)
# 1 x 1 =1
# 1 x 2 = 2
# ..(생략) ..
# 9 x 7 = 63
# 9 x 8 = 72

#문제3
# kakao_price = 1000
# kiwoom_price = 500
#
# for i in range(0,3):
#     kakao_price += 500
#     kiwoom_price += 1000
#
# if kakao_price > kiwoom_price:
#     print("카카오가 더 높다")
# if kakao_price < kiwoom_price:
#     print("키움이 더 높다")
# if kakao_price == kiwoom_price:
#     print("키움과 카카오가 같다")


#문제4
# for i in range (1,10):
#     for j in range(1,10):
#         result = i * j
#         print("%s x %s = %s" % (i,j,result))

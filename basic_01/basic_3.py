#2.4 여러개의 데이터를 리스트로 관리
# 연관성 있는 데이터를 모아서 관리하는 자료형 : 튜플, 리스트, 딕셔너리

#2.4.1 튜플 (자료형 중 가장 빠르며, 미리 정해놓은 데이터만 관리할 때 사용)
#2.25 튜플의 생성과 접근
# a_list = ("키움", "카카오", "대신")
# for val in a_list:
#     print(val)

#2.4.2 리스트 (튜플과 다르게 데이터를 추가하거나 수정 및 삭제 할 수 있음
# 증권사 API 로 부터 데이터를 받을 때 여러 개의 데이터를 포함하는 요청 값은 리스트 형태로 나오는 경우가 많음 그래서 리스트 형태를 잘 다루는 것이 중요함)

# a_list = ["키움", "카카오", "대신"]
# for val in a_list:
#     print(val)
# a_list.append("삼성전자")
# for val in a_list:
#     print(val)


# a_list = ["키움", "카카오", "대신"]
# print(a_list)
#
# a_list[2] = "daum"
# print(a_list)
#
# del a_list[1]
# print(a_list)

#2.4.3 딕셔너리 (데이터가 담아지는 형태가 다름. 튜플과 리스트틑 순서대로 담기지만 딕셔너리는 순서가 존재 하지 않음)
#딕셔너리는 순서가 없고, 키: 데이터 쌍을 가진다.

a_dict = {"키움증권":1300, "카카오증권":1500, "네이버":1000}
# print(a_dict.get("키움증권")) 
# print(a_dict['키움증권'])

for key in a_dict.keys():
    print(a_dict.get(key))


#############################################################################
#2.5 클래스와 함수
# 객체지향 언어는 캡슐화, 상속, 추상화, 다형성 이라는 네가지 특징이 있음
# 객체지향언어는 클래스와 함수를 가짐
# 클래스는 가장 큰 그룹이고 함수는 큰 그룹안에 속해 있는 소그룹으로됨
# 그리고 A그룹(=클래스) 과 B그룹(=클래스)이 있다면 필요에 따라 A그룹의 데이터를
# B그룹에서 사용할 수 있도록 구성이 가능하고 반대로 B그룹의 데이터를 A그룹에서도 사용하게 구성 할 수 있다


# 2.5.1 함수 (define)
# 함수는 변수를 포함하거나 역할에 맡는 알고리즘을 계산하는 작은 단위의 집합체를 말한다.


# def english():
#     print("영어과입니다.")
# english()

# def match(student_name):
#     print(student_name)
# match("토마스")

# def academy(student_name1, student_name2, student_name3):
#     print(student_name1)
#     print(student_name2)
#     print(student_name3)
#
# academy("Thomas", "Edison", "Billy")

# def english(help):
#     help()
#
# def help():
#     print("도와주러 왔습니다")
# english(help)


#2.42 함수에서 데이터 반환받기
# def match():
#     name = "광수"
#     return name
#
# who = match()
# print(who)

#반환받을 데이터 여러개 지정가능
# def multi():
#     return "a","b"
#
# # a, b = multi()
# result = multi()
# print(result)

# 2.5.2 클래스(Class)
# 2.44 클래스의 형식
# class B_school():
#     def __init__(self):
#         print("b대학교 초기화")
#
# B_school()

# class A_school():
#     def __init__(self):
#         print("초기화, 생성자")
#         self.student1_name = None
#         self.student2_name = None
#
#         print(dir(self))
#
# A_school

# class A_school():
#     def __init__(self):
#         print("초기화","생성자")
#         self.student1_name = None

#         b = self.math()
#         print("수학과 학색 %s" % b)

#     def match(self):
#         self.student1_name = "영수"
#         name = self.student1_name

#         return name
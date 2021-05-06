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

class A_school():
    def __init__(self):
        print("초기화","생성자")
        self.student1_name = None

        b = self.math()
        print("수학과 학색 %s" % b)

    def match(self):
        self.student1_name = "영수"
        name = self.student1_name

        return name
    
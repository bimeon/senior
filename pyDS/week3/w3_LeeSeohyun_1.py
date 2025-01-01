# 문제 1
print("# 문제1")
# pi 변수 선언
pi = 3.14

# 질문 입력 받고 diagram 변수에 답 저장
diagram = input("어떤 도형의 특성을 알고 싶으신가요?? (square, circle)")

# diagram에 저장된 string의 값에 따라 계산
# 입력받은 값이 square 라면
if diagram == "square":
    # 사각형의 가로, 세로 값 입력 받기
    width = int(input(f"{diagram}의 가로는 몇인가요?"))
    height = int(input(f"{diagram}의 세로는 몇인가요?"))

    # 사각형의 넓이, 둘레 계산
    area = width * height
    circumference = 2 * (width + height)

    # 결과를 dictionary로 저장
    result_dict = {"사각형 넓이": area, "사각형 둘레": circumference}
# 입력받은 값이 circle 라면
elif diagram == "circle":
    # 원의 반지름 값 입력 받기
    radius = int(input(f"{diagram}의 반지름은 몇인가요?"))

    # 원의 넓이, 둘레 계산
    area = pi * radius * radius
    circumference = 2 * pi * radius

    # 결과를 dictionary로 저장
    result_dict = {"원의 넓이": area, "원의 둘레": circumference}

# 결과 출력
print(f"{diagram}의 특성은 다음과 같습니다.\n{result_dict}")
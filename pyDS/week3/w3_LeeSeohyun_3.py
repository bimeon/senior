# 문제 3
print("# 문제3")
print("기능 : add, average, top_score, list, exit")
# 메뉴 변수를 저장할 변수
func = ""

# 학생 이름과 점수를 저장할 dictionary 정의
student_dict = {}

# func으로 입력한 내용이 exit이 아니라면 계속 반복, exit이라면 종료
while func != "exit":
    # while문이 loop를 돌 때마다 새롭게 func 값을 입력받기
    func = input("\n메뉴를 선택하세요: ")

    # 만약 func 값이 add라면
    if func == "add":
        # 학생 이름, 점수 입력 받기
        name = input("학생 이름: ")
        score = int(input("학생 점수: "))

        # 학생 이름과 점수를 student_dict에 저장하기
        student_dict[name] = score
    # 만약 func 값이 average라면
    elif func == "average":
        # student_dict에 저장된 점수들의 합을 student_dict의 길이(학생 수)로 나누어 평균 점수 계산
        average = sum(student_dict.values()) / len(student_dict)
        # 결과 출력
        print(f"현재 평균 점수: {average}")
    # 만약 func 값이 top_score라면
    elif func == "top_score":
        # 최대 점수를 가지는 학생의 이름을 student_dict에서 가져와 top_score_name 변수에 저장
        top_score_name = max(student_dict, key=student_dict.get)
        # 결과 출력
        print(f"최고 점수 학생: {top_score_name} ({student_dict[top_score_name]})")
    # 만약 func 값이 list라면
    elif func == "list":
        print("학생 목록: ")
        # student_dict의 처음부터 끝까지 for 문으로 돌면서
        for name_dict in student_dict:
            # 결과 출력 (이름: 점수)
            print(f"{name_dict}: {student_dict[name_dict]}")
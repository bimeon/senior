import numpy as np

# 문제 1
print("# 문제1")
# PI 변수 선언
PI = 3.14

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
    area = PI * radius * radius
    circumference = 2 * PI * radius

    # 결과를 dictionary로 저장
    result_dict = {"원의 넓이": area, "원의 둘레": circumference}

# 결과 출력
print(f"{diagram}의 특성은 다음과 같습니다.\n{result_dict}")


# ------------------------------------------------------------------------------------------
# 문제 2
print("\n# 문제2")
# 염기 서열 압축 함수
def compress_dna(dna_sequence):
    # count 변수 딕셔너리 생성
    alphabet_count = {}

    # for문을 통해 dna_sequence에 저장된 문자열을 하나씩 탐색
    for i in dna_sequence:
        # alphabet_count 딕셔너리에 이미 존재하는 key값이면 value에 1을 더함
        try:
            alphabet_count[i] += 1
        # alphabet_count에 없는 key값이라면 value가 1로 저장
        except:
            alphabet_count[i] = 1

    # alphabet과 그 개수가 저장된 alphabet_count 딕셔너리의 key값이 alphabet들만 alphabets 변수에 저장
    alphabets = alphabet_count.keys()
    # compressed 변수 생성
    compressed = ""
    # alphabets에 저장된 alphabet 들을 하나씩 탐색
    for alphabet in alphabets:
        # compressed 문자열에 알파벳과 그 개수를 더하여 문자열 늘리기
        compressed = compressed + alphabet + str(alphabet_count[alphabet])

    # comporessed 문자열 return
    return compressed

# 염기 서열 복원 함수
def decompress_dna(compressed):
    # alphabet, decompressed 변수 생성
    alphabet = ""
    decompressed = ""

    # compressed 문자열을 하나씩 탐색
    for string in compressed:
        # 만약 현재 문자열이 알파벳이라면
        if string.isalpha() == True:
            # alphabet 변수에 현재 문자열 저장
            alphabet = string
        # 만약 현재 문자열이 숫자라면
        elif string.isdigit() == True:
            # times 변수에 알파벳 개수 저장
            times = int(string)
            # decompressed 문자열에 alphabet이 times만큼 반복된 문자열을 추가하여 저장
            decompressed = decompressed + alphabet * times

    # decompressed 문자열 return
    return decompressed

# 압축된 DNA 서열 확인
dna_sequence = "AAACCCGT"
compressed = compress_dna(dna_sequence)
print(f"압축된 DNA 서열: {compressed}")

# 복원된 DNA 서열 확인
decompressed = decompress_dna(compressed)
print(f"복원된 DNA 서열: {decompressed}")


# ------------------------------------------------------------------------------------------
# 문제 3
print("\n# 문제2")
print("기능 : add, average, top_score, list, exit")
# 메뉴 변수를 저장할 변수
func = ""

# 학생 이름과 점수를 저장할 dictionary 정의
student_dict = {}

# func으로 입력한 내용이 exit이 아니라면 계속 반복
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
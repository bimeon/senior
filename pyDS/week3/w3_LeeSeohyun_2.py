# 문제 2
print("# 문제2")
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
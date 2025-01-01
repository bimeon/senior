import numpy as np

# 영화 인덱스, 영화 제목, 상영관 번호
movie_title_array = np.array([
[0, '어벤져스', 3],
[1, '인사이드 아웃', 7],
[2, '겨울왕국', 1],
[3, '인터스텔라', 4],
[4, '매트릭스', 2],
[5, '인사이드 아웃', 5],
[6, '겨울왕국', 6]
])

# 영화 인덱스, 러닝타임(분), 좌석 수, 예매 좌석 수
movie_info_array = np.array([
[0, 180, 200, 150], # 어벤져스
[1, 172, 100, 80], # 인사이드 아웃
[2, 148, 120, 90], # 겨울왕국
[3, 136, 180, 140], # 인터스텔라
[4, 170, 160, 120], # 매트릭스
[5, 172, 200, 180], # 인사이드 아웃
[6, 148, 100, 95] # 겨울왕국
])

# 행 : 영화, 열 : 장르
genre_array = np.array([
[1, 1, 0, 1, 0, 1, 0],
[0, 1, 1, 0, 0, 0, 1],
[0, 0, 1, 0, 0, 0, 1],
[1, 1, 0, 1, 0, 0, 0],
[1, 1, 0, 1, 1, 1, 0],
[0, 1, 1, 0, 0, 0, 1],
[0, 0, 1, 0, 0, 0, 1]
])
# 장르 인덱스 :['액션', '어드벤처', '애니메이션', 'SF', '스릴러', '판타지', '가족']

#  문제 1-1 :가장 인기 있는 영화

reserved_seat = [] #예약 좌석 숫자만을 저장할 빈 리스트 생성
for i in range(len(movie_info_array)): #movie_info_array 길이만큼 반복하며 전체 예약 좌석 숫자를 저장
    reserved_seat.append(movie_info_array[i][3])
reserved_seat=list(map(int,reserved_seat)) #숫자를 int 형식으로 저장하기
maxseat = max(reserved_seat) # 예매 좌석 수 중 최댓값 찾기
maxseat_location = reserved_seat.index(maxseat)  # 예매 좌석 수 중 최댓값의 위치 찾기
top_movie = movie_title_array[maxseat_location][1] # 위치를 기반으로 영화 제목과 상영관 위치 찾기
top_movie_location = movie_title_array[maxseat_location][2] #상영관 위치 찾기
print("가장 인기 있는 영화는",top_movie,"(상영관",top_movie_location,")입니다. (예매 좌석 수:",maxseat)  # 출력하기

#print('가장 인기 있는 영화는 '"%d"'(상영관 "%d"번)입니다. (예매 좌석 수: "%d")' % )

# 문제 1-2 : 100명 이상의 좌석이 예매된 영화

seat_over_100_num = [] #100이상의 좌석 수 저장할 리스트 생성
seat_over_100_name = []  #좌석수가 100 이상인 영화의 이름을 저장 할 리스트 생성
for i in range(len(movie_info_array)): # 100명 이상 예매된 죄석 찾기
    if movie_info_array[i][3] >= 100 :
        seat_over_100_num.append(i)
for j in seat_over_100_num :  # 좌석 위치 기반으로 영화 제목 찾기
    seat_over_100_name.append(movie_title_array[j][1])
print("100명 이상 예매된 영화:", seat_over_100_name)  # 출력하기

# 문제 1-3 : 애니메이션 장르에 속한 영화들의 관객 선호도

anime_no = []  #장르가 애니메이션인 영화의 인덱스를 추가할 리스트 생성
for i in range(len(genre_array)):  # 애니메이션 장르에 속한 영화 찾기
    if genre_array[i][2] == 1 :
        anime_no.append(i)  #장르가 애니메이션이라면 anime_no 리스트에 영화 인덱스를 추가하기
anime_seat = [] #애니메이션 장르의 좌석 수를 저장할 리스트 생성하기
for j in range(len(anime_no)):
    x = int(anime_no[j])
    anime_seat.append(movie_info_array[x][3])  # 평균 예매 좌석 수 계산하기
anime_seat_avg = sum(anime_seat)/len(anime_seat)  #애니메이션 장르 예매 좌석 수의 평균 구하기
print("'애니메이션' 장르 영화들의 평균 예매 좌석 수:", anime_seat_avg)

# 문제 1-4 : 상영관 번호가 2번 또는 5번인 영화의 제목과 예매 좌석 수 추출
# 상영관 번호만 저장된 array 만들기
room_num_array = movie_title_array[:, 2]

# for loop에서 사용할 index 및 상영관의 index를 저장할 room2_index, room5_index 초기화
index = 0
room2_index, room5_index = 0, 0

# for loop 를 돌면서 room_num_array에 저장된 상영관 번호 탐색
for room_num in room_num_array:
# 상영관 번호가 2라면 room2_index에 현재 index 저장
    if room_num == '2':
        room2_index = index
# 상영관 번호가 5라면 room5_index에 현재 index 저장
    if room_num == '5':
        room5_index = index

    # index를 1씩 증가
    index += 1

room2_index = int(room2_index)
room5_index = int(room5_index)

print(f'\'{movie_title_array[room2_index, 1]}\'(상영관 {movie_title_array[room2_index, 2]}번): {movie_info_array[room2_index, 3]},'
f'\'{movie_title_array[room5_index, 1]}\'(상영관 {movie_title_array[room5_index, 2]}번): {movie_info_array[room5_index, 3]}')

# 문제 1-5 : 유클리드 거리 기반 유사한 영화 추천
# 어벤져스 행 저장
avengers_genre_array = genre_array[0, :]
# 나머지 영화 행 저징
other_movies_genre_array = genre_array[1:, :]

# 유클리드 거리 함수 정의
def euclidean_dist(x, y):
    return np.sqrt(np.sum((x-y)**2))

# 거리 list 초기화
distance_list = []
# 6개의 행을 for문으로 검색
for i in range(6):
    # i 번째 행의 영화 장르 행 movie_1_array에 저장
    movie_1_array = other_movies_genre_array[i, :]
    # 거리 list에 유클리드 값 추가(어벤져스와 현재 영화 거리)
    distance_list.append(euclidean_dist(avengers_genre_array, movie_1_array))

# list를 numpy array로 변환
distance_array = np.array(distance_list)
# numpy array의 min 값을 가지는 index 값 찾고, 어벤져스 영화의 인덱스를 더해주기
distance_min_index = distance_array.argmin() + 1

print(f"가장 유사한 영화: '{movie_title_array[distance_min_index, 1]}', 유사도: {round(np.min(distance_array), 2)}")
import pandas as pd

researcher_df = pd.read_csv("problem_2/researchers.csv", encoding='cp949')
performance_criteria_df = pd.read_csv("problem_2/performance_criteria.csv", encoding='cp949')
publications_df = pd.read_csv("problem_2/publications.csv", encoding='cp949')
projects_df = pd.read_csv("problem_2/projects.csv", encoding='cp949')

# 연구원별 프로젝트 기여도 점수 계산
for i in researcher_df['experience_level']: # 경험레벨가중치 설정 - for문을 돌면서 researcher_df의 experience_level접근
    if i == 'Senior': # if 조건문 활용
        researcher_df.loc[i,'researcher_level_weight'] = 2 # i의 열의 researcher_level_weight를 2로 지정
    elif i == 'Junior':
        researcher_df.loc[i, 'researcher_level_weight'] = 1

# PM
# projects_df 의 start_date와 end_date를 합치기
#merge_researcher_df = pd.merge()


researcher_df['project_date'] = projects_df['start_date']-projects_df['end_date']  # start_date-start_date을 통해 프로젝트 일수 계산

researcher_df['pm'] = researcher_df['project_date'] * researcher_df['experience_level'] * 3

# Member
projects_df['member'] = projects_df['project_date'] * researcher_df['experience_level'] * 1.5

# 연구원별 논문 발표 점수 계산






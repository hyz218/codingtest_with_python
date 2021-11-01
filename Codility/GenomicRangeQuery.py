#GenomicRangeQuery

def solution(S, P, Q):
    min_value = 5 # set min_value
    result = [] #set result
    for i in range(len(P)): #P의 길이까지 도는 반복문
        string = S[P[i]:Q[i]+1] #string 생성
        if 'A' in string: #A가 string에 존재하면 min_value를 1로 지정
            min_value = 1
        elif 'C' in string: #C가 string에 존재하면 min_value를 2로 지정
            min_value = 2
        elif 'G' in string: #G가 string에 존재하면 min_value를 3로 지정
            min_value = 3
        elif 'T' in string: #T가 string에 존재하면 min_value를 4로 지정
            min_value = 4
        result.append(min_value) #result list에 min_value 추가하기

    return result
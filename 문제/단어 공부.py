word = input().lower()  # 입력된 단어를 소문자로 변환
count = [0] * 26  # 알파벳 개수를 저장할 리스트 초기화

# 각 알파벳의 개수 세기
for char in word:
    if char.isalpha():  # 알파벳인 경우에만 처리
        index = ord(char) - ord('a')  # 알파벳의 인덱스 계산
        count[index] += 1

max_count = max(count)  # 가장 많이 사용된 알파벳의 개수

# 가장 많이 사용된 알파벳이 여러 개인지 확인
if count.count(max_count) == 1:
    max_index = count.index(max_count)  # 가장 많이 사용된 알파벳의 인덱스
    result_char = chr(max_index + ord('a'))  # 인덱스를 알파벳으로 변환
    print(result_char.upper())  # 대문자로 출력
else:
    print('?')

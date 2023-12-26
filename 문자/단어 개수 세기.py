sentence = input().strip()  # 입력 문자열을 받고 양 끝의 공백을 제거
words = sentence.split()  # 공백을 기준으로 문자열을 단어로 나누어 리스트에 저장
word_count = len(words)  # 리스트에 저장된 단어의 개수 세기

print(word_count)

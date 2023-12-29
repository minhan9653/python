
'''코드 설명 해봐야함'''
import random

def get_response(user_input):
    responses = {
        "안녕": "안녕하세요!",
        "오늘 날씨 어때?": "오늘은 맑아요.",
        "이름이 뭐야?": "저는 챗봇이에요.",
        "사랑해": "나도 사랑해요!",
        "놀자": "뭐하고 놀까요?",
    }

    return responses.get(user_input, "그건 잘 모르겠어요.")

def main():
    print("챗봇: 안녕하세요! 질문이나 대화를 입력해주세요. 나가기를 원하면 '나가기'를 입력하세요.")

    while True:
        user_input = input("사용자: ")
        
        if user_input == '나가기':
            print("챗봇: 나중에 또 이야기 나눠요. 안녕히 계세요!")
            break
        
        response = get_response(user_input)
        print("챗봇:", response)

if __name__ == "__main__":
    main()

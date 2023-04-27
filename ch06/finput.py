# 입력 받아 파일 쓰기
with open("./output/input.txt", 'w') as f:
    while True:
        text = input("저장할 내용을 입력해 주세요(종료-z) : ")
        if text == 'z' or text == 'Z':
            break
        f.write(text)
        f.write('\n')
# 동명 이인 찾기 - 중복값 찾기

def find_same_name(a):
    same_name = []
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                # 중복값 추가
                same_name.append(a[i])
    return same_name

name = ['흥부', '콩쥐', '놀부', '콩쥐']

print(find_same_name(name))
# 순위 정하기
score = [60, 5, 33, 12, 97, 24]
rank = [1, 1, 1, 1, 1, 1]
n = len(score)
print(n)

for i in range(0, n):
    for j in range(0, n):
        if score[i] < score[j]:
            rank[i] = rank[i] + 1


print(rank)
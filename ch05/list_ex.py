# 리스트 복사
a = [1, 2, 3,4]
a2 =[]
"""
for i in a:
    a2.append(3 + i)
print(a2)
"""
a3 = [3 + i for i in a]
print(a3)

a4 = []
"""
for i in a:
    if i % 2== 0:
        a4.append(3 * i)
"""
a4 = [3 * i for i in a if i % 2 == 0]
print(a4)


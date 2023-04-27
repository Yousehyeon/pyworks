import student2
from student2 import Student
"""
# 파일이름.클래스 이름
st1 = student2.Student('이셋', 3)
st1.info()
"""

student = [
    Student("김하나", 1),
    Student("박둘", 2),
    Student("이셋", 3)
]

student[0].info()
student[1].info()

for i in student:
    i.info()
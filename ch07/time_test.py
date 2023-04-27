import time

start = time.time()
def getgob(n):
    gob = 1
    for i in range(1, 6):
        gob *= i
        #print(i, gob)
    return gob

print(getgob(995))
end = time.time()
print(f"소요 시간 : {end-start}")

start = time.time()
def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n-1)

print(facto(995))
end = time.time()
print(f"소요 시간 : {end-start:.20f}")
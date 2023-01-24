
import datetime

# Recursivo
def fibRec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibRec(n-1) + fibRec(n-2)

def fibBuc(n):
    a = 0
    b = 1

    for k in range(n):
        c = b + a
        a = b
        b = c

    return a

start_time = datetime.datetime.now()

#print(fibRec(10))

print(fibBuc(40))
end_time = datetime.datetime.now()
print(end_time - start_time)
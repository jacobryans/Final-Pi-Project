n = [ 'th', 'an', 's', 'e', 'r', 'w', 'to', 'll', 'a' ]
x = 16
answer = ''

for i in range(x):
    a = [ 0, 3, 1, 2, 5, 3, 4, 6, 8, 7, 1, 2, 5, 3, 4, 2 ]
    answer += n[a[i]]
    print answer

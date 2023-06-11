a = [3,2,5]

b = [1,4,4]


t1  = 1
for x in a:
    t1*=x

t2 = 1
for x in b:
    t2 *= x


print(abs(t2-t1))


def find_difference(a, b):
	return abs((a[1]*a[2]*a[0])-b[1]*b[2]*b[0])
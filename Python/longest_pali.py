
def pali(x):
    return x==x[::-1]

s = "baablkj12345432133d"
def subs(s):
  length = len(s)
  return [s[i:j + 1] for i in range(length) for j in range(i,length)]

a = subs(s)

maior = 0

for x in a:
    if pali(x):
        if len(x)>maior:
            maior = len(x)

print(maior)
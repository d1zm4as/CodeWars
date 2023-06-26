def arr_adder(arr):
    return " ".join("".join(i) for i in zip(*arr))
arr = [
  ['J','L','L','M'],
  ['u','i','i','a'],
  ['s','v','f','n'],
  ['t','e','e','']
]

print(arr_adder(arr))
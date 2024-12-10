def a_weird_function(x: list[int]) -> int:
    y = x[0]
    z = x[2]
    return 2 * (y + z)

z = a_weird_function([1, 2, 3])
print(z)

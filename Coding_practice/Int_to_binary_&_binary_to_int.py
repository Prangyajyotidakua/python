def bin_to_int(s):
    return int(s,2)

result =bin_to_int("10110101")
print(result)


def  int_to_binary(n):
    return str(bin(n)).replace("0b",'')

result2 =int_to_binary(4)
print(result2)


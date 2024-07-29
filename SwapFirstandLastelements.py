def swapfandL(li):
    temp = li[0]
    li[0] = li[-1]
    li[-1] = temp
    return li

List = [23,45,21,43,65]
print(swapfandL(List))
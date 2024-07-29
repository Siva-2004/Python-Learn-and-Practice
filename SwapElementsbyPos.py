def swapElementsinList(li,a,b):
    if(a < len(li) and b < len(li) and a>0 and b>0):
        temp = li[a]
        li[a] = li[b]
        li[b] = temp
        return li
    else:
        return "Index Out of Range"

List = [12,62,43,58,52,48,12,2]
print(swapElementsinList(List,3,7))
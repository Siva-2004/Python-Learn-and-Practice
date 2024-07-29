'''
    Given two list of numbers,
    write a program to create a new list such that the new list should contain odd numbers from the first list and 
    even numbers from the second list.

'''

def Listmaker(li1,li2):
    result = []
    for i in li1:
        if i%2 != 0:
            result.append(i)
    
    for i in li2:
        if i%2 == 0:
            result.append(i)
    
    return result
            
            
li1 = [12,24,31,52,63]
li2 = [12,43,21,56,28]
print(Listmaker(li1,li2))
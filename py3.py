lst = [1,2,3,4,5,6,7,8,9,10]
i=0
lst_1 = []
lst_2 = []

print(f"Original List is {lst}")
while i<lst[4]:
    lst_1.append(lst[i])
    i=i+1 
    
print(f"Extracted first five elements: {lst_1}") 

for j in range(len(lst_1)-1,-1,-1):
    lst_2.append(lst[j])
    
print(f"Reversed Extracted elements: {lst_2}")
    

def selection_sort(input_dict):
    items=list(input_dict.items())
    n=len(items)

    for i in range(n):
        min_indx=i
        for j in range(i+1,n):
            if items[j][0] < items[min_indx][0]:
                min_indx=j

            elif items[j][0]==items[min_indx][0]:
                if items[j][1] < items[min_indx][1]:
                    min_indx=j

        items[i] , items[min_indx] = items[min_indx] , items[i]
        
    sorted_dict=dict(items)
    return sorted_dict

input_dict={
    'Raj Nayyar':1,
    'Suraj Sharma':2,
    'Armaan Kumar':3,
    'Raj Sharma':4,
    'Aahana Arora':5,
}
sorted_dict=selection_sort(input_dict)
print(sorted_dict)
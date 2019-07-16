def quick_sort(lst):

    for i in range(len(lst)):
        minimum  =i

        for j in range(i+1,len(lst)):
            if lst[j]<lst[minimum]:
                lst[minimum],lst[j] =lst[j],lst[minimum]
                
                
    return (lst)


lst =[2,1,3,4,2,3,4,644,32,324,422,3,4442,4,2,4,5,3,21,0]
quick_sort(lst)

            

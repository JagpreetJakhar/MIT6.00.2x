def greedySum(L, s):
    mult=[]
    rem_sum=s
    for i in L:
        if i <=rem_sum:
            temp=rem_sum//i
            mult.append(temp)
            rem_sum=rem_sum-i*temp
        else:
            mult.append(0)
    sum_1=0
    for j in range(len(mult)):
        sum_1=sum_1+L[j]*mult[j]
    if sum_1 == s:
        return sum(mult)
    else:
        return 'no solution'

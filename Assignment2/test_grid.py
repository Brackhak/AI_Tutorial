i = 0
i_ref = 0
j = 0
j_ref = 0
count = 0
while i <= 8 and j <= 8 :
    print(i,j)
    if i - i_ref < 2 :
        i+=1
    else :
        if j - j_ref < 2 :
            i = i_ref
            j += 1
        else :
            i_ref += 3
            i = i_ref
            j = j_ref
            count += 1
            if (count)%3 == 0 and count != 0:
                print("New squre")
                j_ref += 3
                j = j_ref
                i_ref = 0
                i = i_ref

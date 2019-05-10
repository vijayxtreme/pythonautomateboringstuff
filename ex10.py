j = 0
for i in range(5):
    j = j + 2
    print('\ni= ', i, 'j = ', j)
    if j == 6:
        continue
    #this line gets skipped if j = 6
    print ('I will be skipped over if j = 6')

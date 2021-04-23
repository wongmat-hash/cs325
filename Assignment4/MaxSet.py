def max_indepedent_set(arr):
    including = 0                               #used for calculating including
    excluding = 0                               #used for calculating excluding

    for i in arr:
        #calculate max possible excluding i
        temp = excluding if excluding > including else including                #grabs the largest always and stores in temp
        #print("temp", temp)
        #accumulator variable to calculate max including i
        including = excluding + i                                               #including now is exluding + i
        #print("including", including)
        excluding = temp                                                        #excluding now is set to temp
        #print("excluding", excluding)
    #return back the maximum possible
    return (excluding if excluding > including else including)                  #sends back maximum possible

arr = [7, 2, 5, 8, 6]
print max_indepedent_set(arr)

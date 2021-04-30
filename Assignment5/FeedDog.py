def feedDog(hunger_index,biscuit_size):                                         #takes in two arrays hunger level and biscuit size
        hunger_index.sort()                                                     #first part of greedy is to apply a sort
        biscuit_size.sort()                                                     #first part of greedy is to apply a sort so we sort both
        dog_count=0                                                             #init a count value
        j=0
        for i in biscuit_size:                                                  #use two loops to loop through our double arrays start with BS
                for k in range(j,len(hunger_index)):                            #go from 0 to the size of hunger index
                        if(i>=hunger_index[k]):                                 #if the number of biscuits is greater or = to the hunger index array k
                                dog_count+=1                                    #we add to our count
                                j=j+1                                           #increment our j value
                                break
                if(j==len(hunger_index)):                                       #if j ends up at the hunger index
                        return dog_count                                            #we've hit the end and return count
        return dog_count                                                            #return count

hunger_index =[1,2]
biscuit_size =[1,2,3]
doggyHunger = feedDog(hunger_index,biscuit_size)
print(doggyHunger)

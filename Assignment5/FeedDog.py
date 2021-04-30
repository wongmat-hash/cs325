def feedDog(hunger_index,biscuit_size):
        hunger_index.sort()
        biscuit_size.sort()
        count=0
        j=0
        for i in biscuit_size:
                for k in range(j,len(hunger_index)):
                        if(i>=hunger_index[k]):
                                count+=1
                                j=j+1
                                break
                if(j==len(hunger_index)):
                        return count

        return count
# for user input uncomment below 2 lines and comment 3rd and 4 th line after this line
# hunger_index = [ int(x) for x in input().split()]
# biscuit_size = [ int(x) for x in input().split()]
hunger_index =[1,2]
biscuit_size =[1,2,3]
No_DogSatisfy = feedDog(hunger_index,biscuit_size)
print(No_DogSatisfy)

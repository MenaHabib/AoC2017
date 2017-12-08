sum =0
sum2 =0
input = input("What's your input?\n")
in_arr = [int(x) for x in str(input)]
steps = len(in_arr)/2
#---------------------------------------------------
#Part One
for y in range(len(in_arr)):
    if y == (len(in_arr)-1):
        if in_arr[y] == in_arr[0]:
            sum += in_arr[y]
    elif in_arr[y] == in_arr[y+1]:
        sum += in_arr[y]
print "Part one answer is: ",sum
#---------------------------------------------------
#Part Two
for z in range(len(in_arr)):
    if z == (len(in_arr)-1):
        if in_arr[z] == in_arr[steps-1]:
            sum2 += in_arr[z]
    elif (z+steps)< len(in_arr):
        if in_arr[z] == in_arr[z+steps]:
            sum2 += in_arr[z + steps]
    elif (z+steps)>= len(in_arr) :
        if in_arr[z] == in_arr[z+steps - (len(in_arr))]:
            sum2 += in_arr[z]
print "Part two andswer is: ",sum2
Z = [3,1,2,4,6,5]
i = 0
free = -1
def move_cars(L):
   	k = Z.index(L[0])  # k is the position of the first car
	free = L[0]  # 'free' is the car that is temporarily removed
	print("Move ", k + 1, " to free")
	while any(x == k + 1 for x in L):
        	x = next(x for x in L if x == k + 1)  #Find te car in k
      		z = Z.index(x)
        	Z[k] = x  # Move x to position k
        	if x == L[0]:
            		print("Move free to ", k + 1)
        	else:
           		print("Move ", z + 1, " to ", k + 1)
      			k = z
        		Z[k] = L[0]
        		L.remove(x)
    	Z[k] = free 

while i < len(Z):
    if(Z[i] == Z[Z[i] - 1]):
        i = i + 1
    else:
        L = [Z[i]]
        mainK = Z[i]
        newK = Z[i]
        x = Z[newK-1]
        if mainK == Z[x - 1]:
            L.append(x)
            print(L)
            move_cars(L)
        else:
            while mainK != Z[x - 1]:
                L.append(x)
                newK = x
                x = Z[newK - 1]
                if mainK == Z[x - 1]:
                    L.append(x)
                    print(L)
                    move_cars(L)
                    break
        i = i + 1
print(Z)

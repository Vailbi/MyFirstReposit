from turtle import width


number_of_pixel = int(input())
n=1
size=list()
while n <= number_of_pixel/2:
    if number_of_pixel%n==0:
        size.append(n)
    n +=1
size= size+[number_of_pixel]
size2=size[::-1]
zip(size,size2)
for lenght,width in zip(size,size2):
    print (str(lenght)+" x",width)


#for length in size:
 #   for width in size2:
        

  #      print(length, width)
#print(size,size2)
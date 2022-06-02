number_of_pixel = int(input())
n=1
size=list()
while n <= number_of_pixel/2:
    if number_of_pixel%n==0:
        size.append(n)
    n +=1
print(size)
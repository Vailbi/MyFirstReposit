number_of_pixel = int(input())
n=1
while n <= number_of_pixel/2:
    if number_of_pixel%n==0:
        print(n)
    n +=1
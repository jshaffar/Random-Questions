import time
COUNT = 1000


average_diff_num = 0
iter = 1000 
for f in range(0, iter):
    start = time.time()
    print("Hello World!")
    end = time.time()
    diff = end - start
    average_diff_num += diff

average = average_diff_num / iter

with open("Hello-World/results.txt", "w") as file:

    file.write(str(average) + " is the average number of seconds it takes python to print Hello World! with " + str(iter) + " iterations.")
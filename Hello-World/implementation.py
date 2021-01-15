import time

start = time.time()
print("Hello World!")
end = time.time()
diff = end - start
with open("Hello-World/results.txt", "w") as file:
    file.write(str(diff))
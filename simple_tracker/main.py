f = open("../config/config.txt","r")
interval = f.readline().split("=")[1].strip()
print(interval)
f.close()
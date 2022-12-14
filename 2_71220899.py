a = int(input("a : "))
r = int(input("r : "))
n = int(input("n : "))
for i in range(0, n): 
      x = (a * pow(r, i))
      x=x+(x-a)
print(x)
print("[Program finished]")
total=0
a=int(input("Rentang dari : "))
b = int(input("Ke "))
for i in range(a,b):
     if i%2==0 and i%5!=0 and i%8!=0:
        total=total+1
print("Jumlah Antara ",a,"-", b," Adalah : " ,total)
print("[Program finished]")
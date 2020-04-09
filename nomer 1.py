def fun (x,z):
	lst=[]
	for i in range(x,z):
		i=i**2
		lst.append(i)
	return lst

x = int(input("masukkan angka pertama: "))
y =  int(input("masukkan angka kedua: "))
z=y+1
a=fun(x,z)
print(a)





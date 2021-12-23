def nhapdl():
	print("                                                ")
	print("-----PHƯƠNG PHÁP TỔNG KUHN------")
	print("_________K_________")
	print("(1+Tp1*s)*(1+Tp2*s)")

	#print("K=")
	K=float(input("K=  "))
	#print("Tp1=")
	Tp1=float(input("Tp1= "))
	#print("Tp2=")
	Tp2=float(input("Tp2= "))
	T1=0
	Kp=1/K
	Tw=T1+Tp2+Tp1
	Ti=2/3*Tw
	Ki=Kp/Ti
	Td=0.167*Tw
	Kd=Td*Kp
	print(">>>>>>>>>>>>>>>>>>>>>")
	print(" kp=",Kp)
	print(" ki=",Ki)
	print(" kd=",Kd)
	A=Tp1*Tp2
	B=Tp1+Tp2
	print("mẫu truyền đối tượng là:(1+Tp1*s)*(1+Tp2*s) = A*s^2 + B*s +1:")
	print("A= ",A)
	print("B= ",B)
nhapdl()



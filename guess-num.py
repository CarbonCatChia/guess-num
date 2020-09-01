import random
r = random.randint(1, 100)
while True:
	w = input("請猜一個1-100的數字: ")
	w = int(w)
	if w == r:
		print("你答對了!")
		break
	elif w > r:
		print("比答案大!")
	elif w < r:
		print("比答案小!")



	

	
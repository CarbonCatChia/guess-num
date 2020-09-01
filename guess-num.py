import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1 #count = count + 1
	w = input("請猜一個1-100的數字: ")
	w = int(w)
	if w == r:
		print("你答對了!")
		print("這是你猜的第", count, "次")
		break
	elif w > r:
		print("比答案大!")
	elif w < r:
		print("比答案小!")
	print("這是你猜的第", count, "次")



	

	
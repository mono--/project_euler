def main():
	a=list()
	a.append(1)
	try:
		k=a.index(1)
	except:
		print("Fehler")
	else:
		print(k+2)

main()

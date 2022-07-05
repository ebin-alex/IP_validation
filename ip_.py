def in_range(n): #check if every split is in range 0-255
	if n >= 0 and n<=255:
		return True
	return False
	
def has_leading_zero(n): # check if eery split has leading zero or not.
	if len(n)>1:
		if n[0] == "0":
			return True
	return False
def isValid(s):
	
	s = s.split(".")
	if len(s) != 4: #if number of splitting element is not 4 it is not a valid ip address
		return 0
	for n in s:
		
		if has_leading_zero(n):
			return 0
		if len(n) == 0:
			return 0
		try: #if int(n) is not an integer it raises an error
			n = int(n)

			if not in_range(n):
				return 0
		except:
			return 0
	return 1


file = open("conversion.txt", "w")
def convertIP():
    val = 0
    for ip in ip_adds:
        deci = []
        bina = []
        octa = []
        hexa = []
        val += 1
        org = ip
        ip = ip.split('.')
        ip = [int(x) for x in ip]
        for i in ip:
            deci.append(str(i))
            bina.append(str(bin(i).replace("0b","")))
            octa.append(str(oct(i).replace("0o","")))
            hexa.append(str(hex(i).replace("0x","")))
        txt = "IP: " + org
        print(txt)
        file.write(txt)
        file.write("\n")
        txt= "Decimal: " + ".".join(deci)
        print(txt)
        file.write(txt)
        file.write("\n")
        txt = "Binary: " + ".".join(bina)
        print(txt)
        file.write(txt)
        file.write("\n")
        txt = "Octal: " + ".".join(octa)
        print(txt)
        file.write(txt)
        file.write("\n")
        txt = "Hexadecimal: " + ".".join(hexa)
        print(txt,"\n")
        file.write(txt)
        file.write("\n")
        file.write("\n")




ip_adds = []
for i in range(10):
    x = int(input("Enter IP address: "))
    ip_adds.append(x)
	
validip = []
for i in ip_adds:
    rn = isValid(i)
    if rn == 1:
        validip.append(i)

if len(validip) == len(ip_adds):
		convertIP()




	

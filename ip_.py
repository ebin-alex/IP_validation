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
		

if __name__=="__main__":

    ip_adds = []
    for i in range(10):
        x = int(input("Enter IP address: "))
        ip_adds.append(x)
	


	

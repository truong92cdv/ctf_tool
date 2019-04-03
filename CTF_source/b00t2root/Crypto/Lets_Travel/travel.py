import md5
import sys
from secrets import flag

places = ['Acropolis','Angkor', 'Colosseum', 'Niagara', 'Everest', 'Petra']
p_hashes = {}

def Hash(x):
    n = 6512312763521763187236218732135217361273621765146342343323434232
    x += "Hello_I_am_here."
    x = int(x.encode('hex'), 16)
    for i in range(48):
        x = pow(x, x, n)
        x += 1
    m = md5.new()
    m.update(hex(x))
    print x
    print m.hexdigest()
    return m.hexdigest()

def print_places(places):
	print("Welcome, If we offer you a visit to any two of the following which places would you choose? ")
	for p in places:
		print("* "+p) 
	print("enter place1: ")
	s1 = sys.stdin.readline().strip()
	print("enter place2: ")
	s2 = sys.stdin.readline().strip()
	return s1, s2

def check(s1, s2, p_hashes):
	if Hash(s1) not in p_hashes.values() or Hash(s2) not in p_hashes.values():
		print("The places chosen is not in our list.")
		quit()
	if s1 == s2:
		print("You can't choose the same place twice, Try again.")
	elif(Hash(s1) == Hash(s2)):
		print("Here's the secret you need: \n")
		print(flag)
	else:
		print("We cannot offer you the visit of given two places") 

def main():
	for p in places:
		p_hashes[p]=Hash(p)

	place1, place2 = print_places(places)
	check(place1, place2, p_hashes)

if __name__ == "__main__":
	main()
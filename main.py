from random import choice as c

ran_list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E']
my_ticket = []
s = ""

while len(my_ticket) < 4:
	char = c(ran_list)
	my_ticket.append(char)


secret = []
secret_str = ""
counter = 0

while secret != my_ticket:
    counter += 1
    secret.clear()
    while len(secret) < 4:
        char = c(ran_list)
        secret.append(char)
    print(secret)


else:
    print("\n")
    print("-" * 35)
    print(f"Found your ticket after {counter} tries")

    for m in my_ticket:
        s += m
    print("Your ticket combination is: " + s)

    for i in secret:
        secret_str += i
    print("Winning combination is: " + secret_str)
    print("-" * 35)



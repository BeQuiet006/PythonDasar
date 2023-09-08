a = open("kocak.txt", "a")
a.write("Halo ini saya menulis")
a.close

a = open("kocak.txt", "r")
print(a.read())
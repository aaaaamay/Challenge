
#2. Una lista, cada elemento es una palabra del archivo 
e = []
with open('email.txt') as r:
    for lines in r:
        e.extend(lines.split())
#print(datos2)
print("Name of the sender:", e[3][0:], e[2][0:-1])
print("Email of the sender:", e[4])
print("Names of the receivers:", e[17], e[18], e[15], e[16], e[22], e[23], e[20], e[21][0:-1])
print("Emails of the receivers:", e[19][0:-1], e[24][0:-1], sep=', ')
print("Names and emails of the CC directions:", e[31], e[30], e[29], e[27], e[28], e[32][0:-1]+',', e[35], e[33], e[34], e[36][0:-1])

f = []
with open('email.txt') as n:
    lines = n.readlines()
    for line in lines:
        e.append(line.strip('\n'))
print(f)


#print("Content of the email: ", e[46:148])

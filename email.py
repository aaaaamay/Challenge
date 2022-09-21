e = []
with open('email.txt') as r:
    for lines in r:
        e.extend(lines.split())
d = []
with open('email.txt') as r:
    lines = r.readlines()
    for line in lines:
        d.append(line.strip('\n'))

print("Name of the sender:", e[3][0:], e[2][0:-1])
print("Email of the sender:", e[4])
print("Names of the receivers:", e[17], e[18], e[15], e[16], e[22], e[23], e[20], e[21][0:-1])
print("Emails of the receivers:", e[19][0:-1]+',', e[24][0:-1])
print("Names and emails of the CC directions:", e[31], e[30], e[29], e[27], e[28], e[32][0:-1]+',', e[35], e[33], e[34], e[36][0:-1])
print("Content of the email:", '\n')

print(d[7])
print(d[8])
print(d[9])
print(e[63], e[64], e[65], e[66], e[67], e[68], e[69], e[70], e[71], e[72], e[73], e[74], e[75], e[76], e[77])
print(d[11])
print(d[12])
print(d[13])
print(d[14], '\n')

print("Regards of the email:", e[148], e[149])
print(e[150], e[151], e[152])
print("Skills:")

#print("Content of the email:", e[46:148]   //72:77)

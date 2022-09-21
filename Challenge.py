text = open("email.txt", "r")
nase = text.readline()
# Name of the sender
print("NAME AND EMAIL OF THE SENDER: ")
def name():
    print(nase[nase.find(", ") + 2:nase.find(" ", nase.rfind(" ") - 1)], sep=" ", end=" ")
    print(nase[nase.find(": ") + 2:nase.find(", ")])
name()

# Email of the sender
def email():
    print(nase[nase.find(" ", nase.rfind(" ")) + 1:nase.find("com") + 3])
email()
print("")

# Names of the receivers
print("NAMES OF THE RECEIVERS")
for i in range(1, 4):
    line4 = text.readline()
NameAndEmail = line4[line4.find(", ") + 2:line4.find("; ")]
print(NameAndEmail[NameAndEmail.find(", ") + 1:NameAndEmail.find(" ", NameAndEmail.find(" ") + 1)], end=" ")
print(line4[line4.find(": ") + 2:line4.find(", ")])
NameAndEmail2 = line4[line4.find("; ") + 2:line4.rfind(";")]
print(NameAndEmail2[NameAndEmail2.find(",") + 2:NameAndEmail2.find(" ", NameAndEmail2.rfind(" ")):], end=" ")
print(NameAndEmail2[:NameAndEmail2.find(",")])
print("")

# Emails of the receivers
print("EMAILS OF THE RECEIVERS")
print(NameAndEmail[NameAndEmail.find(" ", NameAndEmail.find(" ") + 1) + 1:])
print(NameAndEmail2[NameAndEmail2.rfind(" ") + 1:])
print("")

# Names of the CC directions
print("NAMES OF THE CC DIRECTORS")
line5 = text.readline()
CCName = line5[line5.find(", ") + 2:line5.find("; ")]
print(CCName[CCName.find(", ") + 1:CCName.find(" ", CCName.find(" ") + 1)], end=" ")
print(line5[line5.find(": ") + 2:line5.find(", ")])
CCName2 = line5[line5.find("; ") + 2:line5.rfind(";")]
print(CCName2[CCName2.find(",") + 2:CCName2.find(" ", CCName2.rfind(" ")):], end=" ")
print(CCName2[:CCName2.find(",")])
print("")

# Emails of the CC directions
print("EMAILS OF THE CC DIRECTORS")
print(CCName[CCName.rfind(" ") + 1:])
print(CCName2[CCName2.rfind(" ") + 1:])
print("")

# Do a correct format for all the email
# Extract: HTML, CSS, JavaScript, Python, Java, Game Development, Web Development
# Locate "Dual learning"

for i in range(1, 11):
    lines = text.readline().capitalize()
    if i >= 5:
        if lines.count("html") >= 1 or lines.count("css") >= 1 or lines.count("javascript") >= 1 or lines.count("python") >= 1 or lines.count("java") >= 1 or lines.count("game development") >= 1 or lines.count("web development") >= 1:
            lines = lines.replace("html", "HTML")
            lines = lines.replace("css", "CSS")
            lines = lines.replace("javascript", "JavaScript")
            lines = lines.replace("python", "Python")
            lines = lines.replace("java", "Java")
            lines = lines.replace("game development", "Game Develoment")
            lines = lines.replace("web development", "Web Development")
            lines = lines.replace("dual learning", "*Dual Learning*")
            lines = lines.replace(lines[lines.find("@")])
            print(lines, end="")
        else:
            print(lines, end="") 

# Mentions

# Complete regards
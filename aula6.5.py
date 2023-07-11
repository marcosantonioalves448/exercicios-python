string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

for caractere in string2:
    string1 = string1.replace(caractere, "")

print(string1)
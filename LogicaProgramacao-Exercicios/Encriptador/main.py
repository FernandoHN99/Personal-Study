from string import *

def createListEncrypted(listCaracteres):
    listReturn = []
    for i in listCaracteres:
        charEncrypted = input(f'Insira o caractere criptografado para {i}: ').upper()
        while (len(charEncrypted) != 1 or charEncrypted in listReturn):
            charEncrypted = input(f'Caractere inválido, insira outro caractere criptografado para {i} : ')
        
        listReturn.append(charEncrypted)
    return listReturn


def createDictFromList(listKey, listValue):
    return dict(zip(listKey, listValue))

def encryptedString(stringOriginal, dictEncrypted):
    stringEncrypted = ""
    for i in stringOriginal:
        stringEncrypted += dictEncrypted[i]
    return stringEncrypted

def decryptedString(stringEncrypted, dictDecrypted):
    stringDecrypted = ""
    for i in stringEncrypted:
        stringDecrypted += dictDecrypted[i]

    return stringDecrypted


if __name__ == '__main__':
    stringOriginal = input('Insira a a frase original: ').upper()

    listKeysEncrypted = list(ascii_uppercase + digits + punctuation + whitespace)
    listValuesEncrypted = ['8', 'e', 'n', 'x', 'u', 'j', '^', "'", '~', 'm', '/', 'k', '+', 't', 'r', '|', 'a', '1', '?', 'g', '\x0b', 'o', '4', '(', 'q', '.', '{', '!', '\r', ']', '0', '-', 'w', '}', '$', 'l', 'v', 'c', 'y', '7', ';', ' ', '*', ')', '%', '#', '9', '@', '6', '>', '\\', '=', '\x0c', 'i', 'd', 'p', ',', '<', 's', '5', 'h', 'b', '\t', '&', '`', ':', 'f', '\n', '_', '3', '[', '2', 'z', '"']
    converterReady = ""
    while(converterReady != 'S' and converterReady != 'N'):
        converterReady = input('Quer utilizar um conversor já pronto? (S/N): ').upper()
    if converterReady == 'N':
        listValuesEncrypted = createListEncrypted(listKeysEncrypted)
    
    
    dictEncrypted = createDictFromList(listKeysEncrypted, listValuesEncrypted)
    dictDecrypted = createDictFromList(listValuesEncrypted, listKeysEncrypted)

    stringEncrypted = encryptedString(stringOriginal, dictEncrypted)
    stringDecrypted = decryptedString(stringEncrypted, dictDecrypted)

    print(f"String Original: {stringOriginal}")
    print(f"String Criptografada: {stringEncrypted}")
    print(f"String Descriptografada: {stringDecrypted}")

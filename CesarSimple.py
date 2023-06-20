alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ","."]  #definition de l'alphabet

def cryptage(message, cle):                  #definition fonction de cryptage
    traduction = ""
    for lettre in message:
        k = alphabet.index(lettre)
        traduction += alphabet[(k + cle) % len(alphabet)]
    return traduction    

def decryptage(message, cle):                #definition fonction de decryptage
    traduction = ""
    for letter in message:
        k = alphabet.index(letter)
        traduction += alphabet[(k - cle)%len(alphabet)]
    return traduction    

def bruteforce(message):                #definition fonction de Bruteforce si on a pas la cle de cryptage
    for cle in range(len(alphabet)):
        traduction = ""
        for lettre in message:
            if lettre in alphabet:
                k = alphabet.index(lettre)
                traduction += alphabet[(k - cle) % len(alphabet)]
            else:
                traduction += lettre
        print(f"Clef {cle}: {traduction}")   #le f est une fonction pour formater une string
                                             #nb le None est normale car on renvoye rien mais on affiche uniquement


print("\n")  #retours a la ligne pour separer 
print("*****Programme Cryptage Cesar simple*****")     #mise en place d'un mini menu
choix = int(input("Voulez vous Crypter, Decrypter ou Bruteforce? choix(1, 2 ou 3): "))

if choix == 1:
    messageCrypter = input("Entrez votre message à crypter : ")
    messageCrypter = messageCrypter.lower()
    b = int(input("Entrez la clé de chiffrement : "))
    print("votre message crypteé est: "+ cryptage(messageCrypter, b))
elif choix == 2:
    messageDecrypte = input("Entrez votre message à décrypter : ")
    x = int(input("Entrez la clé de chiffrement : "))
    print("votre message decryptee est : "+ decryptage(messageDecrypte, x))
elif choix == 3:
    messageBrut = input("Entrez votre message à bruteforcer : ")
    bruteforce(messageBrut)
else:
    print("Veuillez entrer un choix valide entre ceux proposees entre parentheses.")

print("\n")



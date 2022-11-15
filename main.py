def input_texte_clair():
	texte_clair = str(input("\nTexte a chiffrer (seulement des caracteres sans accent) : ")).upper()
	return texte_clair

def input_texte_chiffre():
	texte_chiffre = str(input("\nTexte a dechiffrer : ")).upper()
	return texte_chiffre

def input_cle():
	cle = str(input("\nCle de chiffrement / dechiffrement (chaine de caracteres sans accent) : ")).upper()
	return cle

def choix_mode():
	mode = ""
	while mode != "1" and mode != "2":
		mode = input("\nMode (saisissez le numero du mode) :\n1 - Chiffrer\n2 - Dechiffrer\n>>> ")	
	return mode

def creation_chaine_cle(texte, cle): # Création d'une chaîne avec n fois la clé de la même taille que le texte à chiffrer - ex : MONTAGNE -> CLECLECL
	nb_fois_cle = (len(texte) - (len(texte) % len(cle))) // len(cle) 
	chaine_cle = cle * nb_fois_cle
	for i in range(len(texte) % len(cle)):
		chaine_cle += cle[i]
	return chaine_cle


def fonction_chiffrement(lettre_code_ascii, lettre_cle_code_ascii):
	lettre = ((lettre_code_ascii % 64) + (lettre_cle_code_ascii % 64)) % 26 # Revenir automatiquement au début de l'alphabet 	
	return lettre

def fonction_dechiffrement(lettre_code_ascii, lettre_cle_code_ascii):
	lettre = (lettre_code_ascii - lettre_cle_code_ascii) % 26
	return lettre

def conversion_chiffrement(lettre, lettre_cle): 
	lettre_code_ascii, lettre_cle_code_ascii = ord(lettre), ord(lettre_cle) # Conversion caractères -> code ASCII
	lettre_chiffree = fonction_chiffrement(lettre_code_ascii, lettre_cle_code_ascii) # Chiffrement de la lettre
	lettre_caractere_chiffree = chr(lettre_chiffree + 64) # Conversion code ASCII -> caractère
	return lettre_caractere_chiffree

def conversion_dechiffrement(lettre, lettre_cle):
	lettre_code_ascii, lettre_cle_code_ascii = ord(lettre), ord(lettre_cle) # Conversion caractères -> code ASCII
	lettre_dechiffree = fonction_dechiffrement(lettre_code_ascii, lettre_cle_code_ascii) # Déchiffrement de la lettre
	lettre_caractere_dechiffree = chr(lettre_dechiffree + 64) # Conversion code ASCII -> caractère
	return lettre_caractere_dechiffree

def algo_chiffrement(texte_clair, chaine_cle):
	texte_chiffre = "" # Déclaration chaîne de caractères chiffrée
	for lettre, lettre_cle in zip(texte_clair, chaine_cle): 
		if lettre != " ":
			lettre_chiffree = conversion_chiffrement(lettre, lettre_cle)
			texte_chiffre += lettre_chiffree
		elif lettre == " ": 
			texte_chiffre += " "
	return texte_chiffre

def algo_dechiffrement(texte_chiffre, chaine_cle):
	texte_dechiffre = "" # Déclaration chaîne de caractères déchiffrée
	for lettre, lettre_cle in zip(texte_chiffre, chaine_cle):
		if lettre != " ":
			lettre_dechiffree = conversion_dechiffrement(lettre, lettre_cle)
			texte_dechiffre += lettre_dechiffree
		elif lettre == " ": 
			texte_dechiffre += " "
	return texte_dechiffre


""" Instructions """

mode = choix_mode() # Choix du mode - Chiffrer (1) ou déchiffrer (2)

if mode == "1":
	texte_clair = input_texte_clair() # Saisie du texte à chiffrer
	cle = input_cle() # Saisie de la clé de chiffrement
	chaine_cle = creation_chaine_cle(texte_clair, cle)
	texte_chiffre = algo_chiffrement(texte_clair, chaine_cle) # Récupération du texte chiffré dans une variable	
	print(texte_chiffre)
else:
	texte_chiffre = input_texte_chiffre() # Saisie du message à déchiffrer
	cle = input_cle() # Saisie de la clé de déchiffrement (doit être identique à la clé de chiffrement car chiffrement symétrique)
	chaine_cle = creation_chaine_cle(texte_chiffre, cle)
	texte_dechiffre = algo_dechiffrement(texte_chiffre, chaine_cle) # Récupération du texte déchiffré dans une variable
	print(texte_dechiffre)
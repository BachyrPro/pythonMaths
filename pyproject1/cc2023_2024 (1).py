#1-Creez les variables Q et R respectivement pour valeurs les matrices Q et R ci-dessus
Q=[[1.2,0.5,3.0],[1.0,2.5,7.7],[1.1,6.5,8.1]]
R=[[2.1,5.0],[0.1,5.2],[1.1,5.6]]
# Question 2
def ProducMat(A,B):
    """effectue la multiplication de deux matrices A et B"""
    # Nombre de lignes de A
    n = len(A)
    # Nombre de colonnes de B
    p = len(B[0])
    # Nombre de colonnes de A (qui doit etre egal au nombre de lignes de B)
    m = len(B)

    # Initialisation de la matrice résultat avec des zéros
    produit_P = [[0 for i in range(len(B[0]))] for i in range(len(A))]
    # Multiplication des matrices
    for i in range(n):
        # pour chaque ligne de A
        for j in range(p):
            # pour chaque colonne de B
            for k in range(m):
                # pour chaque élément à multiplier
                produit_P[i][j] += A[i][k] * B[k][j]
    return produit_P
# Question 3
def ProductMatEx(A,B):
    # Vérification de la compatibilité des dimensions
    if len(A[0]) != len(B):
        return "Erreur : Les matrices ne peuvent pas etre multipliées"
    # Initialisation de la matrice résultat avec des zéros
    produit_P = [[0 for i in range(len(B[0]))] for i in range(len(A))]
    # Multiplication des matrices
    for i in range(len(A)):
        # pour chaque ligne de A
        for j in range(len(B[0])):
            # pour chaque colonne de B
            for k in range(len(B)):
                # pour chaque élément à multiplier
                produit_P[i][j] += A[i][k] * B[k][j]
    return produit_P
# Questin 4- creer le ichier...
def creer_fichiers_matrices():
    # Definiton des matrices Q et R
    Q = [
         [1.2,0.5,3.0],
         [1.0,2.5,7.7],
         [1.1,6.5,8.1]
    ]
    R = [
         [2.1,5.0],
         [0.1,5.2],
         [1.1,5.6]
    ]
    # Creation du fichier pour la matrice Q
    # 'w' signifie le mode écriture avec (write)
    with open('fichierA.txt','w') as f:  # with open permet de gerer proprement l'ouverture et la fermeture des fichiers
        for ligne in Q:
            # Convertit chaque nombre en string et les joint avec des virgules
            ligne_txt = ','.join(str(x) for x in ligne)  # Combine tous les élements d'une liste en une seule chaine
            # Ecrit la ligne dans le ichier avec un retour à la ligne (\n)
            f.write(ligne_txt + '\n')
    # Creation du fichier pour la matrice R
    with open('fichierB.txt', 'w') as f:
        for ligne in R:
            # Convertit chaque nombre en string et les joint avec des virgules
            ligne_txt = ','.join(str(x) for x in ligne)
            f.write(ligne_txt + '\n')

## Fonction pour lire une matrice depuis un fichier
def lire_matrice(nom_fichier):
    """Lit une matrice depuis un fichier"""
    matrice = [] # Liste de matrice vide pour stocker la matrice
    # 'r' signifie mode lecture(read)
    with open(nom_fichier, 'r') as f:
        for ligne in f: # Pour chaque ligne du fichier
            # strip() enlève les espaces et \n
            # split(',') sépare la ligne aux virgules
            ligne = ligne.strip().split(',')
            #convertit chaque ligne en liste de nombre floattants
            ligne = [float(x) for x in ligne]
            # Ajoute la ligne a la matrice
            matrice.append(ligne)
    return matrice
# Test fonctions
creer_fichiers_matrices()
# Lecture et vérification des matrices
try: # Protège contre les erreurs courantes
    Q = lire_matrice('fichierA.txt')
    R = lire_matrice('fichierB.txt')
    print("Matrice Q lue depuis fichierA.txt :")
    for ligne in Q:
        print(ligne)
    print("\nMatrice R lue depuis le fichierB.txt :")
    for ligne in R:
        print(ligne)
except FileNotFoundError: # Si un fichier n'existe pas
    print("Erreur : Un des fichiers n'a pas pu etre trouvé")
except ValueError: # Si le format des données est incorrect
    print("Erreur : Format de données incorrect dans un des fichiers")
# Question 5 : produit matricielle du fichierA.txt et du fichierB.txt
try:
    # Creation des fichiers
    creer_fichiers_matrices()
    # Lecture des matrices depuis des fichiers
    A = lire_matrice('fichierA.txt')
    B = lire_matrice('fichierB.txt')
    # Calcul du produit
    resultat = ProducMat(A,B)
    # Affichage du resultat
    print("°Produit des matrices :")
    for ligne in resultat:
        # Arrondir les nombres à 2 décimales pour plus de clarté
        print([round(x, 2) for x in ligne]) # round() arrondit un nombre décimal(loat) a un nombre specifié à 2 décimales
except FileNotFoundError: # Si un fichier n'existe pas
    print("Erreur : Un des fichiers n'a pas pu etre trouvé")
except ValueError: # Si le format des données est incorrect
    print("Erreur : Format de données incorrect dans un des fichiers")
except IndexError: # Si les dimensions des matrices sont incompatibles
    print("Erreur : Les dimensions des matrices ne permettent pas la multiplication")
#PROGRAMME 2: Multiplication de deux matrices
def multiplier_matrices(A, B):
    """effectue la multiplication de deux matrices A et B"""
    # Vérification de la compatibilité des dimensions
    if len(A[0]) != len(B):
        return "Erreur : Les matrices ne peuvent pas etre multipliées"
    # Initialisation de la matrice résultat avec des zéros
    resultat = [[0 for i in range(len(B[0]))] for i in range(len(A))]
   # Multiplication des matrices
    for i in range(len(A)):
# pour chaque ligne de A
       for j in range(len(B[0])):
# pour chaque colonne de B
           for k in range(len(B)):
# pour chaque élément à multiplier
               resultat[i][j] += A[i][k] * B[k][j]
    return resultat
 # Definition de la matrice A
A = [
     [1,3,3],
     [1,4,3],
     [1,3,4]
]
# Dédinition de la matrice B
B = [
     [0,2,1],
     [7,-3,2],
     [2,-1,1]
]
 # Calcul de la multiplication
resultat = multiplier_matrices(A, B)
 # Affichage des resultats
print("Matrice A :")
for ligne in A: # Affiche la matrice de A
     print(ligne)
print("\nMatrice B :") # Le \n crée une ligne vide avant d'afficher "Matrice de B:"
for ligne in B:
    print(ligne)
print("\nResultat de A * B :")
for ligne in resultat:
    print([round(x, 2) for x in ligne]) # Prend chaque nombre x dans la ligne, round(x, 2) pour arrondir ce nombre à deux décimales, puis creer une nouvelle liste avec ces nombres arrondis


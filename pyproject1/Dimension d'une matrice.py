#déterminer la dimension d'une matrice
def get_dimensions(matrice): # get:obtenir les dimensions d'une matrice
    # Déterminer le nombre de lignes et de colonnes d'une matrice
    nb_lignes = len(matrice) #nombre de lignes
    nb_colonnes = len(matrice[0]) #nombre de colonnes de la première ligne
    return nb_lignes, nb_colonnes
# Définition de la matrice A
A = [
    [1, 3, 3],
    [1, 4, 3]
]
# Obtention des dimensions
lignes, colonnes = get_dimensions(A)
# Afichage des résultats
print("Matrice A :")
for ligne in A:
    print(ligne)
print(f"\nDimensions de la matrice A :")
print(f"Nombre de lignes : {lignes}")
print(f"Nombre de colonnes : {colonnes}")
print(f"la matrice A est donc de dimension {lignes}*{colonnes}")
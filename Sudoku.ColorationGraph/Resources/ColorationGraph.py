import networkx as nx
import matplotlib.pyplot as plt

# Définition de la grille Sudoku
sudoku_grid = (
    (5, 3, 0, 0, 7, 0, 0, 0, 0),
    (6, 0, 0, 1, 9, 5, 0, 0, 0),
    (0, 9, 8, 0, 0, 0, 0, 6, 0),
    (8, 0, 0, 0, 6, 0, 0, 0, 3),
    (4, 0, 0, 8, 0, 3, 0, 0, 1),
    (7, 0, 0, 0, 2, 0, 0, 0, 6),
    (0, 6, 0, 0, 0, 0, 2, 8, 0),
    (0, 0, 0, 4, 1, 9, 0, 0, 5),
    (0, 0, 0, 0, 8, 0, 0, 7, 9)
)

def build_sudoku_graph(grid):
    G = nx.Graph()
    
    # Ajout des nœuds
    for i in range(9):
        for j in range(9):
            G.add_node((i, j))

    # Ajout des arêtes pour les lignes et les colonnes
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if k != j:
                    G.add_edge((i, j), (i, k))  # arêtes pour la même ligne
                if k != i:
                    G.add_edge((i, j), (k, j))  # arêtes pour la même colonne

    # Ajout des arêtes pour les sous-grilles
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    for k in range(i, i + 3):
                        for l in range(j, j + 3):
                            if (x, y) != (k, l):
                                G.add_edge((x, y), (k, l))

    return G

def sudoku_coloring(graph, grid):
    coloring = nx.coloring.greedy_color(graph, strategy="largest_first")
    
    for node, color in coloring.items():
        i, j = node
        grid[i][j] = color + 1  # Ajouter 1 car les couleurs vont de 1 à 9

def print_sudoku(grid):
    for row in grid:
        print(row)

# Construire le graphe Sudoku
sudoku_graph = build_sudoku_graph(sudoku_grid)

# Résoudre le Sudoku avec la coloration de graphe
sudoku_coloring(sudoku_graph, sudoku_grid)

# Afficher la solution
print_sudoku(sudoku_grid)

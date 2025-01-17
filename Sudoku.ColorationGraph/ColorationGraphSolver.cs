﻿using Python.Runtime;
using Sudoku.Shared;

namespace Sudoku.ColorationGraph;

public class ColorationGraphSolver : PythonSolverBase
{
public override Shared.SudokuGrid Solve(Shared.SudokuGrid s)
{
    using (Py.GIL())
    {
        dynamic scope = Py.CreateScope();
        PyObject pyCells = s.Cells.ToPython();
		scope.Set("sudoku_grid", pyCells);
            
	    // Assignation du chemin complet au script Python à la variable scriptPath
        string scriptPath = @"C:\Users\kokob\Test final\2024-ECE-Ing4-Fin-Sudoku-Gr02\Sudoku.ColorationGraph\Resources\ColorationGraph.py";

        // Lecture du script Python à partir du chemin spécifié et exécution dans l'espace de nom Python
        string code = System.IO.File.ReadAllText(scriptPath);
        scope.Exec(code);

        // Appelle la fonction Python et récupère la grille résolue
        PyObject result = scope.Eval("solve_sudoku_python(sudoku_grid)");

        // Convertit le résultat Python en tableau C#
        var managedResult = result.As<int[][]>();
        return new Shared.SudokuGrid() { Cells = managedResult};
        }
    }
}

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 10:58:45 2021

@author: Maximilian.Hofheinz
"""

# Definition des Sudokus:
grid = [[2,0,5,3,0,8,4,0,9],[0,7,0,0,0,0,0,5,0],[9,0,4,0,0,0,6,0,7],[5,0,0,0,4,0,0,0,2],[0,0,0,5,0,7,0,0,0],[6,0,0,0,3,0,0,0,8],[4,0,6,0,0,0,8,0,1],[0,2,0,0,0,0,0,6,0],[8,0,1,2,0,9,7,0,4]]

# Importation der numpy Libary und print in Matrix-Form:
import numpy as np
print(np.matrix(grid))

# Funktion mit der ermittlet wird ob an der gewünschten Stelle die gewünschte Zahl eingesetzt werden kann:
def possible(y,x,n) :
    global grid
    for i in range(0,9) :
        if grid[y][i] == n :
            return False
    for i in range(0,9) :
        if grid[i][x] == n :
            return False
    x0 = (x//3)*3 
    y0 = (y//3)*3
    for i in range(0,3) :
        for j in range(0,3) :
            if grid[y0+i][x0+j] == n :
                return False
            
    return True

# User-Aufforderung zum Lösen des Sudokus:
print("To solve the sudoku tipe in solve()")

# Löst mit Hilfe der possible Funktion das sudoku:
def solve() :
    global grid
    for y in range(9) :
        for x in range(9) :
            if grid[y][x] == 0 :
                for n in range(1,10) :
                    if possible(y,x,n) :
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return 
    print("Your Solution:")
    print(np.matrix(grid))
    
    
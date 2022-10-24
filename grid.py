from random import randint
import numpy as np
import pygame
import random

class Grid():
    def __init__(self, scale, offset, width, height, screen):
        self.scale = scale
        self.rows = int(width/self.scale)
        self.columns = int(height/self.scale)
        self.size = (self.rows,self.columns)
        self.grid_arr = np.ndarray(shape=(self.size))
        self.offset = offset # size of each of each cell
        surface = screen

    def array_generate(self): # generates random cell formation in grid
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_arr[x][y] = random.randint(0,1) # each index stores whether cell is alive or dead 

    def conway(self,surface, pause): 
        for x in range(self.rows): # draws current configuration of grid with dead and alive cells
            for y in range(self.columns):
                posx = x*self.scale
                posy = y*self.scale
                if self.grid_arr[x][y] == 1:
                    pygame.draw.rect(surface, (0,121,150), [posx, posy, self.scale-self.offset, self.scale-self.offset])
                else:
                    pygame.draw.rect(surface, (255,255,255), [posx, posy, self.scale-self.offset, self.scale-self.offset])
        state = np.ndarray(shape=(self.size))
        if pause==False:
            for x in range(self.rows):
                for y in range(self.columns):
                    neighbour = self.get_neighbour(x, y) # checks number of living neighbours
                    if self.grid_arr[x][y]==1 and (neighbour<2 or neighbour>3): # if number of living neighbours are less than 2(underpopulation) or greater than 3(overpopulation), it kills a living cell
                        state[x][y] = 0
                    elif self.grid_arr[x][y]==0 and neighbour==3:# if number of living neighbours are equal to 3 then a cell is born(reproduction)
                        state[x][y] = 1
                    else:
                        state[x][y] = self.grid_arr[x][y]
            self.grid_arr = state

    def mouse_handle(self, x_mouse, y_mouse):
        x_ = x_mouse//self.scale
        y_ = y_mouse//self.scale
        if self.grid_arr[x_][y_]!=None:
            self.grid_arr[x_][y_] = 1
    
    def get_neighbour(self, x, y):
        total = 0
        for n in range(-1,2):
            for m in range(-1,2):# checking number of living cells
                xcoord = (x+n+self.rows) % self.rows # mod method is used if the index exceeds the size and hence the cells towards the left edge are used to handle this degenerate case
                ycoord = (y+m+self.columns) % self.columns
                total += self.grid_arr[xcoord][ycoord]
        total -= self.grid_arr[x][y]
        return total

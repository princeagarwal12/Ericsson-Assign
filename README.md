# Ericsson-Assignment
 
This repository contains the code for the python application as part of Ericssion Assignment for the internship.

## Problem Statement: 

Develop an application that finds the route between any two given point A and B that has the optimized number of trees on the route. 

## Algorithm:

I used a modified version of A* Algorithm for my analysis. A-star is one of the most successful search algorithms to find the shortest path between nodes or graphs. It is an informed search algorithm, as it uses information about path cost and also uses heuristics to find the solution. But in our case we want to find out the path which is short as well as contains maximum number of trees possible.

Each time A* enters a node, it calculates the cost, f(n) (n being the neighboring node), to travel to all of the neighboring nodes, and then enters the node with the lowest value of f(n).

Normally f(n) is defined as:     **f(n) = g(n) + h(n)** <br />
In our Case, it is defined as:   **f(n) = g(n) + h(n) + t(n)**

where,  **f(n)** = lowest cost in the neighboring node n <br />
		**g(n)** = exact cost of the path from the starting node to any node n <br />
		**h(n)** = heuristic estimated cost from node n to the goal node <br />
	    **t(n)** = negative cost or reward if the neighbor node n is a tree node <br />
	    i.e. we want to follow such a route with trees on it but at the same time it is optimal (shorter) 

**Assumptions:** 
* Optimal path is such that it is shorter also and contains maximum possible trees 
* Nodes are equidistant as adjacent spots on grid represent nodes

## Running The code:
![A-star](https://github.com/princeagarwal12/Ericsson-Assign/blob/master/gif1.gif)
* Left Click on the blocks to place the start point (ORANGE)/ end point(BLUE) /barriers(BLACK)
* Right click to remove any spot
* Middle Click to place a tree node (GREEN)
* Press spacebar to start the algorithm
* Press c to reset/clear the grid 
* Path is shown in purple
* Red and Yellow spots represents the explored nodes during algorithm run 

## Dependencies:

* [Python 3](https://www.python.org/) - The Programming Language used.
* [PyGame](https://www.pygame.org/news) - Pygame is a cross-platform set of Python modules designed for writing video games.

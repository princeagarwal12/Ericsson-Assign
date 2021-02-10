# Ericsson-Assignment
 
This repository contains the code for the python application as part of Ericssion Assignment for the internship.

## Problem Statement: 

Develop an application that finds the route between any two given point A and B that has the optimized number of trees on the route 

## Algorithm and Assumptions:

I used a modified version of A* Algorithm for my analysis. A-star is one of the most successful search algorithms to find the shortest path between nodes or graphs. It is an informed search algorithm, as it uses information about path cost and also uses heuristics to find the solution. But in our case we want to find out the path which is short as well as contains maximum number of trees possible.

Each time A* enters a node, it calculates the cost, f(n)(n being the neighboring node), to travel to all of the neighboring nodes, and then enters the node with the lowest value of f(n).

Normally f(n) is defined as:    f(n) = g(n) + h(n)
In our Case, it is defined as:   f(n) = g(n) + h(n) + t(n)

where, f(n) = lowest cost in the neighboring node n
	   g(n) = exact cost of the path from the starting node to any node n
	   h(n) = heuristic estimated cost from node n to the goal node.
	   t(n) = negative cost or reward if the neighbor node n is a tree node 
	   i.e. we want to follow such a route with trees on it but at the same time it is optimal (shorter)

 

![Alt text](https://github.com/princeagarwal12/Ericsson-Assign/blob/main/example.jpg?raw=true "Example")
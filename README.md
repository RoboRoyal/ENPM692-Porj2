# ENPM692-Porj2

Project 2 for ENPM692, Spring 2021

This project implements breath-first on an eight-way connected graph 400x300 unites with static obstacles.

For this project, pygame is used to visualise the graph, along with the nodes explored and the final path found.

Pygame is the only library used that is not built in.

To run:
```
python3 main.py
pygame 2.0.1 (SDL 2.0.14, Python 3.7.4)
Hello from the pygame community. https://www.pygame.org/contribute.html
Enter the X coordinate of the start point: 4
Enter the Y coordinate of the start point: 20
Enter the X coordinate of the target point: 6
Enter the Y coordinate of the target point: 9
Finding path...
Found path
Visited:  296
Path:  12
Done
```
The program will ask for what type of algorithm to use, followed by the start and target location.
If you enter an invalid point, it will re-prompt you.

In the shown map, white represents free space, black is for obstacles, cyan is explored nodes, and the final path is depicted in red.

Known issues:
While there is a function to perform an a* search, there are some issues with it.
Because of this, it is not included as an option.
a* does not always return the shortest possible path.
I think there is a problem with the adding better nodes to the list in order.
A* search is also very slow due to the need to sort and iterate through the open list every step.


Github repository: https://github.com/RoboRoyal/ENPM692-Porj2


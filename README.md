# ENPM692-Porj2

Project 2 for ENPM692, Spring 2021

This project implements breath-first and a* search on an eight-way connected graph 400x300 unites with static obstacles.

For this project, pygame is used to visualise the graph, along with the nodes explored and the final path found.

Pygame is the only library used that is not built in.

To run:
```
python3 main.py
pygame 2.0.1 (SDL 2.0.14, Python 3.7.4)
Hello from the pygame community. https://www.pygame.org/contribute.html
Choose 1 for a* or 2 for breath first search: 2
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
If you enter an invalid point, it will re-prompt you

Known issues:
a* does not always return the shortest possible path.
I think there is a problem with the heuristic. 





# Rubik's Cube Simulator - Command Line Interface
## About
I made this short and simple Rubik's Cube simulator for the 2x2, 3x3, 4x4, 5x5 and 6x6 puzzles back in Grade 10 during a school term break. This project was an exercise in the fundamentals of OOP and making use of classes in Python 3, featuring the use of inheritance and polymorphism.

## Functionality
When the program first starts up, a menu will ask for which cube to interact with; for example entering `cube3` yields the 3x3 cube.

In the main screen of the program, a Rubik's Cube made in ASCII art (and colored using the `colorama` module) is displayed. Enter the command `?` (or equivalently `help`) to give a full list of commands.

The program is able to perform the following actions:
| Main command | Aliases | Required Arguments | Optional Arguments      | Action Performed |
| ------------ | ------- | ------------------ | ------------------      | ---------------- |
| `?`          | `help`  | N/A                | N/A                     | Shows the help message. |
| `scramble`   | `scr`   | N/A                | `{move}` (positive int) | Scrambles the cube with `{move}` moves. <br> If `{move}` is not provided then a suitable random number of moves is performed. |
| `{cube notation}` | N/A | N/A               | N/A                     | Performs the turns dictated by `{cube notation}`. <br> For example entering `U F' R2` does those three moves on the cube. Specifications on how to format `{cube notation}` are given in the help message. |
| `solve`        | N/A     | N/A                | N/A                     | Yields an instructional procedure and explanation on how to solve the cube from the current state, returning it to a solved state in the process. <br> Only supported for the 2x2 (Ortega method) and the 3x3 (Beginner's method with 4-step LL) |
| `reset`        | `rst`     | N/A                | N/A                     | Resets the cube's state to the default solved state (white on the top, green in front) |
| `turnTime`     | N/A     | `{ms}` {non-negative int) | N/A              | Sets how long each move takes to visually perform to `{ms}` milliseconds when using `scramble`/`scr` |
| `change`       | N/A     | N/A                | N/A                     | Takes the user back to the cube selection menu where a different cube can be chosen to interact with. <br> The state of all cubes are saved even after switching cubes. |
| `exit`         | `end`     | N/A                | N/A                     | Exits the program (cube states are NOT stored). |

## Implementation Note - Rotating Faces
The $N \times N$ cube's state is stored as a 2D array; a list of 6 face arrays each with $N^2$ entries. Each face array's indexing corresponds with the order of the colored tiles on each face as left-to-right, top-to-bottom.

<img src="https://github.com/user-attachments/assets/8caed51d-5df9-46b8-b5b5-262cca877330" width=25%> <br>
> Example of how the indices of a face array `[0,1,2,3,4,5,6,7,8]` correspond to the positions of the tiles on the face (for a 3x3 cube).

Typically, the method to rotate a square matrix $A\in M_{N\times N}$ clockwise by $90^{\circ}$ is to take the transpose then reverse the rows;
```math
A \longmapsto A^{\top} = \left( x_{0\leq i,j \leq N-1}\right) \longmapsto \left( x_{i,N-j-1}\right) 
```
However implementations of this method would be difficult for the 1D array datatype which I chose previously. Instead, I created an algorithm to generate mappings from the indices of an unrotated to where those indices map to upon clockwise or anticlockwise rotation by $90^{\circ}$.
For example, I found the indices rotation maps for the 2x2 are
```math
[0,1,2,3] \longmapsto [2,0,1,3] \quad \text{(clockwise map)} \qquad\qquad
[0,1,2,3] \longmapsto [1,3,0,2] \quad \text{(anticlockwise map)}
```
Specifically, the algorithm generates these maps during the initialization of the cube object, and the methods which rotate faces utilize these maps.

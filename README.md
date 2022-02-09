# noughts_and_crosses
A simple Noughts and Crosses application for desktop. Completed December 2021 - before I'd learnt about git and repositories (which would have been handy).

My first coding project with the simple aim of completing a fully functioning application.

## Description

The application consists of a simple GUI with a few settings that can be selected by the user: 
  - One player: The user will play against the computer.
  - Two player: The user will play against another person (on the same device).
  - Noughts: The user will be noughts, and hence play the first move.
  - Crosses: The user will be crosses, and hence play the second move.

## Under the hood

### About the AI

The computer is programmed to play perfectly, so I'm sorry to say that it will be impossible to win for you loners out there. You can draw though!

Due to the small search space of Noughts and Crosses a minimax search algorithm could be implemented. At each move (apart from if the computer plays first where it selects a square randomly) it calculates the end state resulting from each available move, where it then selects the best option outcome wise. 

This was a good algorithm for me to implement as it is quite simple in theory but still managed to cause a few headaches for me to debug.

### The GUI

I had no experience with GUI's before this and I used the PySimpleGUI module to create this. After a little bit of reading, it seemed rather unsurpringly simple. Obviously the application doesn't involve anything particularly complex, but I would use the module again.

# gomoku_game

This is a python version of gomoku (five-in-a-roll) game designed to be part of the RoboGomoku project. The project aims to build a robot to play gomoku game against human. The few parts included in the project are: gomoku game code, robotic arm control algorithm, camera based piece detector and a gomoku board. 

The code designed in this repository is going to be able to play the gomoku game against human within the terminal. No GUI is going to be developed here. The I/O data will be tranferred to the arm through ROSserial. 


piece_detect is opencv sample. To run it, type ./output. if main.cpp is modified, using
g++ main.cpp -o output `pkg-config --cflags --libs opencv` to generate a new output file.

gomoku_game is game code. It is developed by python. Type `python gomoku.py` to run.

mbed LPC1768 is used in this project. Download main.cpp in mbed_communication and complie it with mbed online complier. Download the generated binary code to mbed root file.

Openmv code is under openmv file. Dowdload openmv IDE from https://openmv.io/pages/download. Import openmv_find_circle.py to detect pieces.

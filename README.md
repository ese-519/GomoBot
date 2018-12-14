# gomoku_game

This is a python version of gomoku (five-in-a-roll) game designed to be part of the RoboGomoku project. The project aims to build a robot to play gomoku game against human. The few parts included in the project are: gomoku game code, robotic arm control algorithm, camera based piece detector and a gomoku board. 

The code designed in this repository is going to be able to play the gomoku game against human within the terminal. No GUI is going to be developed here. The I/O data will be tranferred to the arm through ROSserial. 



g++ main.cpp -o output `pkg-config --cflags --libs opencv`
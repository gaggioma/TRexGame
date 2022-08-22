# 🐍Python autopilot implementation on 🦖 [T-Rex Game](https://trex-runner.com)

## Main purpose
During this summer hollyday, i asked me if was possibile to design and to implement an outopilot ✈️ software to a simple web game in less time as possible. 
For this purpose i have chosen [T-Rex Game](https://trex-runner.com) with the autopilot sw written in [Python](https://www.python.org/).
This game require that t-rex jumps Cactus🌵 before impact on them. 

## Implementation idea
Basically the idea is composed on three steps, repeated indefinitely:

1) [Make a snapshot of current game screen](#game-snapshot)
2) [Define target](#define-target-area)
1) [Simulate keyboard interaction](#keyboard-interaction)

### Game snapshot
To get a game state, a snapshot of current window is done.
I used [Selenium](https://selenium-python.readthedocs.io/) which make this task simpler. 

### Define target area
From the snapshot image we should determine an area inside which to see if exist some cactus 👀🌵.
For this puprose, from the main image has been cropped a rectangular window centered in (732, 380) top left center, and dimension (w=192, h=25).
The detection of Cactus has been realized evaluating the Min value from image pixel matrix. The blank image has Min = 83 otherwise some cactus has been detected. 

### Keyboard interaction
Once some cactus has been detected the user has to make T-Rex jumps by a keyboard interaction (up arrow).
This has been easily implemented using [Pynput](https://pynput.readthedocs.io/en/latest/).
Another point where this library cames me in help is at the begining of the game, where a space bar click is mandatory to start.

## Result
Here a demo of application.
Unfortunately, when game speed increase, Selenium sample rate in not enough or at the moment i have not tried to find a remedy 😄.

https://user-images.githubusercontent.com/64643932/185933423-a11d2352-4dfb-4871-9035-ffb1b5a73ce3.mp4






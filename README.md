# Zombies - A pygame animation
Zombies is a pygame simulation of the evolution of the population of survivors (humans), zombies and dead in the case of a zombie apocalypse.
The python script comes with 3 different models of apocalypse: in the first, dead come back to life and become zombies, which can also infect humans;
in the second one, dead people can't resurrect and all the zombies come from infection of healthy people; and in the third one infection rate (beta)
is smaller than the defensive abilities of humans (alpha), resulting in the winning of humans.

The simulation is done through the numerical approximation of the following system of differential equations:

![equation](http://latex.codecogs.com/gif.latex?%5Cleft%5C%7B%20%5Cbegin%7Barray%7D%7Bl%7D%20%5Cfrac%7BdS%7D%7Bdt%7D%20%3D%20%5Calpha%20S%20%5Cleft%28%20%5Cfrac%7BS&plus;R&plus;Z%7D%7Bc%7D%20%5Cright%29-%5Cbeta%20S%20Z-%5Cdelta%20S%20%5C%5C%20%5Cfrac%7BdZ%7D%7Bdt%7D%20%3D%20%5Cbeta%20S%20Z&plus;%5Cxi%20R-%5Calpha%20S%20Z-%5Csigma%20Z%20%5C%5C%20%5Cfrac%7BdR%7D%7Bdt%7D%20%3D%20%5Cdelta%20S&plus;%5Calpha%20S%20Z&plus;%5Csigma%20Z-%5Cxi%20R%5C%5C%20%5Cend%7Barray%7D%20%5Cright.)

using Runge-Kutta method with order 4.

Computation is done using Cython to speed up the process, and the result are passed back to Python via an array. Then the animation begins.
Speed of the animation can be controlled using the arrow keys, up to x8 speed.

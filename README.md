# Python implementation of EVM(Eulerian Video Magnification)

This is a python implementation of eulerian video magnification《[Eulerian Video Magnification for Revealing Subtle Changes in the World](http://people.csail.mit.edu/mrub/evm/)》.
>Our goal is to reveal temporal variations in videos that are difficult or impossible to see with the naked eye and display them in an indicative manner. Our method, which we call Eulerian Video Magnification, takes a standard video sequence as input, and applies spatial decomposition, followed by temporal filtering to the frames. The resulting signal is then amplified to reveal hidden information.Using our method, we are able to visualize the flow of blood as it fills the face and also to amplify and reveal small motions. Our technique can run in real time to show phenomena occurring at temporal frequencies selected by the user.


## Required Libraries
* OpenCV for pyramids and io
* SciPy for signal processing
* NumPy for image processing


## Testing
To see the module work run the command:
```
python -m evm.evm <videofile> <type> <lowband> <highband> <pyramidlevels> <alpha>
```

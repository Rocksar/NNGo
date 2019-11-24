# NNGo
Policy Network, Convolutional Neural Network.

Requirement to get it working:
- Python 3.5 environment with TensorFlow and Keras properly installed
- Files to read the data are stored under .npy (binary files)
- The Parser of Data used the SGF format 

Compatibility with the GoGui interface (Try to beat my policy network, normally its easy :) ):
- Command to compile it the python link need to be the one with Tensorflow and Keras Installed
  - Path\python.exe Path\jouer.py gtp

The TfRecord part of the work is not working but after some research this not seams to be relevent
because the npy approach is as good as the TFRecord one.

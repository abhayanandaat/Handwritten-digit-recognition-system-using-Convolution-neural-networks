# Handwritten-digit-recognition-system-using-Convolution-neural-networks

This is the project on Handwritten digit recognition system using Convolution neural networks. Me and my team have done it in the ExpertsHub Internship at Hyderabad.

## Tools and framework:

1. Jupyter Lab: Can be installed using Anaconda https://www.anaconda.com/distribution/ It's one of the best ways to get through Jupyter notebooks.

2. Google Colab: It was a treat and a half using this beacuse of its simplicity. I could also run this on my mobile and edit the files supporting .ipynb format It's even a lot helpful for the ones not owning a GPU. Google Colab can be found here: https://colab.research.google.com/

3. NumPy: Its already installed on your computer if you have Anaconda installed. You can type

conda list 

to find all the required packages installed.

4. TensorFlow: Its not pre-installed with the Anaconda, just type

conda install tensorflow 

and select the version of the package to be installed on your computer. You can find more about TensorFlow here: https://www.tensorflow.org

5. Keras: Its an high level deep neural network API built on top of TensorFlow. You need to run the command

conda install keras 

in your CLI. You can know nore about keras here: https://keras.io

6. matplotlib

7. PyCharm(2018.3.4) You can install PyCharm from here: https://www.jetbrains.com/pycharm/download/

## Dataset:

I took the MNIST dataset of handwritten digits. The dataset contains 70000 images of 28 * 28 pixels. I've taken 60000 images for training and 10000 for testing my model. Loading the dataset was easier, thanks to the builtin command to load MNIST data.

(trainData, trainLabels), (testData, testLabels) = mnist.load_data()

## How to use this?

1. Firstly, run all the cells corrresponding to Final Project.ipynb for more than 50 epochs for greater accuracy.

2. After the cells run, you can have a look on the plots of the accuracy and the loss of the test of my model. Unknown Unknown-1

3. Now open your CLI and run the app.py file stored on your computer. Please specify the current directory location of the file for no hassle.

4. When it has run succesfully you would see something similar to this:


5. Type the following command in your browser.
https://localhost:5000/result/?d= and the image link you like to test.

6. You'll find a number being printed in the same tab of the browser.

7. You can test for various kinds of images digts available.

## Presentation

You can also find the presentation of the project of my team in the files. Its been titled as expertppt.key

## Future work:

1. Will continue to modify this project.

2. Will try to look into the front-end version of this project so that it can be more fancy to play with.

3. Also will try to work on multiple digit recognition and also the detection of letters in the English Alphabet.

4. Also will create an Android app which would work will all the mentioned things above.

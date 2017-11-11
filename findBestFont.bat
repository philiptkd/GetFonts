@echo off

setlocal enabledelayedexpansion

rem - compile the program
javac C:\Users\Phil\Desktop\NeuralNets\MNIST_net\src\Main.java

rem - initialize the weights by training
java -cp C:\Users\Phil\Desktop\NeuralNets\MNIST_net\src Main 1 5 C:\Users\Phil\Desktop\NeuralNets\MNIST_net\src\mnist_train.csv C:\Users\Phil\Desktop\NeuralNets\MNIST_net\src\mnist_test.csv C:\Users\Phil\Desktop\NeuralNets\MNIST_net\src\weights C:\Users\Phil\Desktop\NeuralNets\MNIST_net\src\output.csv

rem - test against every font set
for /R %%i in (*.csv) do (
	java -cp C:\Users\Phil\Desktop\NeuralNets\MNIST_net\src Main 2 4 C:\Users\Phil\Desktop\NeuralNets\MNIST_net\src\mnist_train.csv %%i C:\Users\Phil\Desktop\NeuralNets\MNIST_net\src\weights C:\Users\Phil\Desktop\NeuralNets\MNIST_net\src\output.csv
)

endlocal
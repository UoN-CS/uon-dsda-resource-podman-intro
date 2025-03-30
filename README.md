Basic Podman Configuration
==========================

This repository shows a very simple configuration to run a python script within a podman container.

In this case, the simple python program loads numbers from a file called numbers.txt and returns the mean.

The repository contains the following files:

| Filename         | Description                                    |
| ---------------- | ---------------------------------------------- |
| Containerfile    | script to describe the container configuration |
| data             | folder containing the data (numbers.txt)       |
| requirements.txt | file containing required libraries             |
| process.py       | The python file to be executed                 |

You should be able to create a container by executing:

	podman build -t my-python-app -f Containerfile
	
which will generate an image from the specification in ``Containerfile``

If you execute

	podman images
	
You should see a list of images including the one just created.



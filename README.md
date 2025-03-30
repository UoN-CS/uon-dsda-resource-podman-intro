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

To start the container from an image use:

    podman run my-python-app

This should run the container and return the result.  In this example the result is printed to STDOUT, but also saved in a file called results.txt

You should be able to see all past containers that have run ran by executing:

    podman container ps -a

Look for the most recent entry which will look something like this:

    2b3520f12279  localhost/my-python-app:latest  python process.py  7 minutes ago   Exited (0) 2 minutes ago                   quirky_austin

To retrieve the output file from the container, you can use

    podman cp <CONTAINERNAME>:/app/results.txt ./results.txt

so in the case of the container above:

    podman cp <quirky_austin>:/app/results.txt ./results.txt

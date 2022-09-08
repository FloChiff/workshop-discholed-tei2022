# How to run 
## Creating a virtual environment

A virtual environment should be created for running the python scripts we use for the workshop. 

As stated in the Python [documentation](https://docs.python.org/3/library/venv.html):

```
A virtual environment is a Python environment such that the Python interpreter, libraries and scripts installed into it are isolated from those installed in other virtual environments, and (by default) any libraries installed in a “system” Python, i.e., one which is installed as part of your operating system.
```

To create a virtual environment, use the following command line in your terminal (note: be sure to be working in the workshop directory):
```commandline
virtualenv -p python3 venv
```

`venv` being the name of your virtual environment.

Now, you can activate your virtual environment with:

```commandline
source venv/bin/activate
```

## Installing dependencies

Now that your virtual environment is created and activated, you can install all python libraries we are using for the workshop in your dedicated virtual environment.

Enter the following command: 

```commandline
pip install -r requirements.txt
```
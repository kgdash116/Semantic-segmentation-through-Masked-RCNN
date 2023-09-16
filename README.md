# AIVR package
A Python package that integrates with the Unity environment. This package,
allows the user to communicate with the Unity environment, it has many functions,
and leverages Machine Learning libraries such as Open-CV, ZeroMQ and numpy.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)


## Installation

- Make sure that Python is installed on the target machine, this package
 supports:
 ```
 python = "^3.9"
 ````
- If Poetry is not already installed on the target machine, you can install it    using pip. Run the following command:
```
pip install poetry
```
- Open a terminal on the target machine, navigate to your project directory, i.e the **aivr** root folder which contains the **pyproject.toml** file, and run the following command to install the project dependencies:
```
poetry install
```
- Poetry will read the pyproject.toml file and set up a virtual environment for your project, installing all the specified dependencies.

## Usage

- Assuming, Unity is installed, open the Unity environment and open the project named:
```
Python-OpenCV-2022-2-16
```
- Press the play button.
- Simultaneously run your Python script as you normally would by navigating to the aivr project directory, that has the
```
Publisher.py
```
file, and run your script using Python:
```
poetry run python Publisher.py
```
- Poetry takes care of creating a virtual environment for your project, ensuring that dependencies are isolated and well-managed.
- The python script will guide you through the next processes, ad will provide options for operations that are available.

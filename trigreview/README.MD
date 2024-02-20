# Project Setup Guide

This guide outlines the steps for setting up the Python environment using `pyenv`, managing virtual environments with `venv`, and installing the required packages for the project.

## Python Version Management with pyenv

1. **Install `pyenv`**: Follow the instructions on the [`pyenv` GitHub page](https://github.com/pyenv/pyenv#installation) to install `pyenv`.

2. **Install Python 3.9.18**: Use `pyenv` to install Python 3.9.18.

    ```bash
    pyenv install 3.9.18
    ```

3. **Set Global Python Version**: Optionally, set Python 3.9.18 as the global version.

    ```bash
    pyenv global 3.9.18
    ```

## Virtual Environment Setup with venv

1. **Create a Virtual Environment**: Navigate to your project directory and create a virtual environment.

    ```bash
    cd /path/to/your/project
    pyenv local 3.9.18  # Ensure the local Python version is set
    python -m venv venv
    ```

2. **Activate the Virtual Environment**:

    ```bash
    source venv/bin/activate
    ```

## Package Installation

Ensure the virtual environment is activated before installing packages.

1. **Upgrade pip**:

    ```bash
    pip install --upgrade pip
    ```

2. **Install Required Packages**: Install `matplotlib`, `numpy`, and any other required packages.

    ```bash
    pip install matplotlib numpy
    ```

## Launching JupyterLab

After installing the necessary packages, you can start JupyterLab.

```bash
jupyter-lab

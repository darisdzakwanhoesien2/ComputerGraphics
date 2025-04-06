# ComputerGraphics

Currently the Assignment is well-implemented on Python 3.9.6 (unlike Python 3.7). Here is the steps to implement this code

1. Setup the Conda environment
conda create -n gisl_env python=3.9.6
conda activate gisl_env

2. Let's navigate to the folder
cd CG_Programming_Assignment_1

2. Let's install the required document 
pip install PyOpenGL PyOpenGL_accelerate # to substitute: PyOpenGL-3.1.5-cp37-cp37m-win_amd64.whl, PyOpenGL_accelerate-3.1.5-cp37-cp37m-win_amd64.whl
pip install PyGLM  # Used version 2.8.1, as 0.4.5b1 does not exist
pip install -r requirements.txt

3. Please use .gisl in this file, as it's adjusted to #version 120, not #version 430 core as template given
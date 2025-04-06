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

The work on Python 3.7 become ongoing implementation. 
1. Try this first (conda create -n gisl_env python=3.9.6). If not, use this CONDA_SUBDIR=osx-64 conda create -n gisl_env_py37 python=3.7 -c conda-forge
2. cd GG
3. pip install -r requirements.txt
4. Install any missing files: pip install PyGLM==2.8.1 PyOpenGL==3.1.9 PyOpenGL_accelerate==3.1.9 (instead of .whl)
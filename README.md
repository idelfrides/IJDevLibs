# IJ Development Lib


This is the package I use to help me on my projects.
This package contain several functions to build any application you as a Dev need.


## STEPS TO USE THIS lib LOCALY

### 1 | Clone the remote repository to your workspace

     git clone https://github.com/idelfrides/IJDevLibs


### 2 | Create your virtualenv like ( use Python 3.x )

     virtualenv [your_venv_name]

### 3 | Virtualenv activation

     source [your_venv_name]/bin/activate

If you are using fish, write

     source [your_venv_name]/bin/activate.fish

### 4 | To Install requirements, switch to IJDevLibs. In your terminal, type

     cd IJDevLibs/


### 5 | Upgrade pip

     pip install -U pip or pip install --upgrade pip


### 5 | Install requirements

     pip install -r requirements.txt


### 6 | Take o look at modules to see and understand wicth functions you have in the lib. Go inside lib and take a look careful


### 7 | Now, to use some function you need to make it importation, from this package. like that

     from IJDevLibs.IJGeneralLib import (
          create_diretory,
          write_content_infile,
          write_log_file
     )

### 8 | [WARNING ] If you get some Error from the lib, it should be because of PATH SYSTEM. I recomend you run a folling module:

     python IJDevLibs/update_sys_path.py

### 9 | UPDATE this package in your workspace whenever you need. Remove the lib, then make clone like STEP #1.

     rm -R IJDevLibs/

### 10 | Execute STEP 1

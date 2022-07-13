# IJ General Usage Package


This is the package I use to help me on my projects.
This package contain several functions to build any application you as a Dev need.


## STEPS TO USE THIS PACKAGA LOCALY

### 1 | Clone the remote repository to your workspace

     git clone https://github.com/idelfrides/IJGeneralUsagePackage.git


### 2 | Create your virtualenv like ( use Python 3.x )

     virtualenv [your_venv_name]

### 3 | Virtualenv activation

     source [your_venv_name]/bin/activate

If you are using fish, write

     source [your_venv_name]/bin/activate.fish

### 4 | Install requirements

     pip install -r requirements.txt

### 5 | Take o look at modules to see and understand wicth functions you have in the lib. Go inside lib and take a look careful


### 6 | Now, to user some function you need to make it importation, like that

     from IJGeneralUsagePackage.ijhandlefiles import (
          create_diretory,
          write_content_infile,
          write_log_file
     )

### 7 | [WARNING ] If you get some Error from the lib, it should be because of PATH SYSTEM. I recomend you run a folling module:

     python IJGeneralUsagePackage/prepare_environment.py

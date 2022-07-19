# IJ General Usage Package


This is the package I use to help me on my projects.
This package contain several functions to build any application you as a Dev need.


## STEPS TO USE THIS PACKAGA LOCALY

### 1 | Clone the remote repository to your workspace

     git clone https://github.com/idelfrides/IJGeneralUsagePackage


### 2 | Create your virtualenv like ( use Python 3.x )

     virtualenv [your_venv_name]

### 3 | Virtualenv activation

     source [your_venv_name]/bin/activate

If you are using fish, write

     source [your_venv_name]/bin/activate.fish

### 4 | To Install requirements, switch to IJGeneralUsagePackage. In your terminal, type

     cd IJGeneralUsagePackage/


### 5 | Install requirements

     pip install -r requirements.txt

### 6 | Take o look at modules to see and understand wicth functions you have in the lib. Go inside lib and take a look careful


### 7 | Now, to use some function you need to make it importation, from this package. like that

     from IJGeneralUsagePackage.IJGeneralLib import (
          create_diretory,
          write_content_infile,
          write_log_file
     )

### 8 | [WARNING ] If you get some Error from the lib, it should be because of PATH SYSTEM. I recomend you run a folling module:

     python IJGeneralUsagePackage/update_sys_path.py

### 9 | UPDATE this package in your workspace whenever you need. Remove the lib, then make clone like STEP #1.

     rm -R IJGeneralUsagePackage/

### 10 | Execute STEP 1

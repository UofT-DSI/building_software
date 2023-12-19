**Lesson 3 Instructor Notes Live Coding Instructions:**

1. Have students fork the instructor’s repository for this lesson, which should contain the preprocess.py,analyze.py, andsample\_data.txt files.
1. Install Make. <https://www.gnu.org/software/make/>
1. Live-coding session. Have students code along as the instructor creates a makefile with the following content:

all: preprocess analyze

preprocess:

python preprocess.py

analyze:

python analyze.py

clean:

rm -f processed\_data.txt

4. Runmake.

a. Observe how Make automates the running of the scripts.

5. Give students time to modify the Makefile or scripts for further experimentation.
5. Clean Up: Runmake clean to remove the generated processed\_data.txt file.

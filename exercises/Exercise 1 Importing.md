## Exercise 1: Importing

#### Goal

Get comfortable with different ways of importing objects from a package.

#### Preparation

0. [if not done already] fork the repository
   
   https://github.com/aspp-latam/2023-mexico-organizing-documenting-distributing

   and clone it to the laptop in a new directory

1. You will be editing files within this directory
2. Open a terminal and change to this directory, so that you can run the scripts that you are editing

#### Tasks

1. Work on the file `brewing/example_usage_inside_package.py`:

   1. import and call the `make_example_potion` function from the module `brew_potions.py` function ➔ open a terminal, change to the `brewing` directory and run the script `example_usage_inside_package.py`: what happens?
   2. change the import statement so that you can call the `make_example_potion` function like this: `br.make_example_potion` ➔ run the script again: what happens?

2. Work on the file `example_usage_outside_package.py`, which is in the directory where you cloned the repo:
   1. import the brewing package from the `example_usage_outside_package.py` that lives at the top level directory of the repo ➔ in the terminal, change to the top level directory of the repo and run the script `example_usage_outside_package.py`: what happens?
   2. import and call only the `make_example_potion` function from the module `brew_potions.py`, which is in the `brewing` directory ➔ run the script again: what happens?
   3. does it work? if yes, why? If no, why not?

3. Work on the file `scripts_and_notebooks/example_usage_different_folder.py`:
   
   1. try to import and call only the `make_example_potion` function afrom the module `brew_potions.py` ➔ in the terminal, change to the `scripts_and_notebooks` directory and run the script `example_usage_different_folder.py`: what happens?
   2. does it work? if yes, why? If no, why not?

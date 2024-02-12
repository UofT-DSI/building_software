# Building Robust Software Homework 1

## Task 1
* Convert code from your Python Assignment 2 (Pandas and Visualization) into a Python *script*
* Consider saving figures using `plt.savefig('filename.png')`

## Task 2
* Create a git repository and commit your Python script to the repository

##### Hint
* Create a repository on the web GitHub interface
* Follow the instructions to clone the empty repository to your local computer
* `git add -A`
* `git commit -m "<commit message>`
* `git push origin <branch name>`

## Task 3
* Select 3 or more variables
* Decide whether each variable would be more suitable as a command-line argument, job-specific configuration, or user configuration

##### Suggestions
* Filename of the input CSV dataset
* Column name to group by
* Function to aggregate data by
* Plot colours, labels, etc...

## Task 4
* Using argparse, modify your script to read command line arguments
    * This should, at the very least, include the filename of the job-specific configuration
    * This should also include any variables you decided should be a command-line argument

##### Hint
```python
import argparse

parser = argparse.ArgumentParser(description='Dataset analysis script')
parser.add_argument('config', type=str, help='Path to the configuration file')
args = parser.parse_args()

# read arguments
print(args.config)
```

## Task 5
* Using pyyaml, load and parse job-specific and user configuration files

##### Hint
```python
import yaml

config_paths = ['user_config.yml']
config_paths += args.config

config = {}
for path in config_paths:
    with open(path, 'r') as f:
        this_config = yaml.safe_load(f)
        config.update(this_config)

print(config)
```

## Task 6
* Modify your script to use the variables you parsed using `argparse` and that you loaded from the configuration files`

##### Hint
* Where you previously specified a literal (fixed, static value), use the variable instead
```python
# previously
df.groupby('Route')

# new
df.groupby(config['group_col'])
```

## Task 7
* Commit your changes
* Push to GitHub

## Submission
Paste in your repository URL into a Google Doc in your submission folder. Indicate in the document that you completed Homework 1.

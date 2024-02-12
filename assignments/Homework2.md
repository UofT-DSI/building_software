# Building Robust Software Homework 2

## Task 1: Errors
Open the script you created in Building Software Homework 1 (the script version of Python Assignment 2)

1. Identify at least one location where you could raise an error or make an assertion, then implement.
1. Identify at least one location where you could catch errors using `try` and `except`.
1. In your `except` block, use `e.add_note()` to add context to the exception, then raise the exception.


## Task 2: Logging
Open the script you created in Building Software Homework 1 (the script version of Python Assignment 2)

1. Import the `logging` module
1. Add an argument to your `argparse` called `--verbose`
1. Identify at least one location in your Python Assignment 2 *script* where it would be appropriate to log DEBUG, INFO, or WARNING messages and add the logging commands to your script
    * eg. `logging.info(f'Loading {filename}')`


##### Hint
```python
# Argument parser (most of this should be from Homework 1)
parser = argparse.ArgumentParser(description='My Python Analysis')
parser.add_argument('--verbose', '-v', action='store_true', help='Print verbose logs')
args = parser.parse_args()

# Determine logging level based on arguments
logging_level = logging.DEBUG if args.verbose else logging.WARNING

# Initialize logging module
logging.basicConfig(
    level=logging_level, 
    handlers=[logging.StreamHandler(), logging.FileHandler('my_python_analysis.log')],
)

######## elsewhere in your code ########
logging.info('Message')

```

## Submission
Paste in your repository URL into a Google Doc in your submission folder. Indicate in the document that you completed Homework 2.


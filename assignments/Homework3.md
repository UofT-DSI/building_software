# Building Robust Software Homework 3

## Task 1: Refactor into a function
Using your script from BRS Homework 2:
1. Identify at least one section of your code that can be modularized into a function
    * Suggestions:
        * Data loading
        * Creating derivative columns
        * Grouping / aggregation
1. Copy your code into a function
    * You may need to reformat or change the variable names
    * Ensure all the required variables are passed into your function
1. Replace your code at the original location with the relevant function call

#### Example
##### Original
```python
df = pd.read_csv('data.csv')
df.rename({'ID': 'bus_id'}, inplace=True)
```

##### Refactored
```python
def load_and_rename(dataset_path):
    df = pd.read_csv(dataset_path)
    if 'ID' not in df.columns:
        raise ValueError('ID column not found')
    df.rename({'ID': 'bus_id'}, inplace=True)

    return df

df = load_and_rename('data.csv')
```

## Task 2: Write a unit test
1. Create a Python testing script
    * Hint: it can be named anything you wish, but must start with `test_`
1. In the testing script, import your refactored function
    * Hint: `from analysis_script import myfunction`
1. Write one or more unit tests for your function

```python
def test_myfunction_results():
    out = myfunction(inputs)
    assert out == 'expected output'

def test_myfunction_errors():
    with pytest.raises(ValueError):
        load_and_rename('dataset_without_ID_column.csv')
```

## Task 3: Run your unit test
Run your unit test by calling `pytest` from your terminal.

```bash
$ cd /path/to/repo
$ pytest
```

## Optional exercise for fun: Automated tests with GitHub actions
1. Copy the sample `demos/github_action_pytest.yml` from the BRS3 lesson directory into your new repository at `.github/workflows/pytest.yml`
1. Commit the pytest workflow
1. Push to GitHub
1. Check your GitHub Actions status in your repository online


## Submission
Paste in your repository URL into a Google Doc in your submission folder. Indicate in the document that you completed Homework 3.

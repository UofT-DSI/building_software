# Building Software Summative Assignment
By the end of this course, you will build an installable Python package that analyzes data retrieved from the GitHub API (or another web data provider of your choice). You'll work in teams and collaborate using tools on GitHub.

## Requirements
The deliverable, your package:
1. Must be hosted on a GitHub repository.
1. Must be installable using pip: `pip install https://github.com/user/yourteamrepo`
1. Must include a module named `Analysis`
1. Must include a README.md, LICENSE, and CONDUCT.md file
1. Must include unit tests
1. Must use the `logging` library to output debug, info, and error messages as appropriate
1. Must be documented using Python docstrings in the numpy style
1. Must use `try`/`except` and assertions to catch errors and must raise useful error messages
    * Hint: We can't analyze data that has not yet been loaded! And consider incorrect configuration parameters!

During development, your team must:
1. Track features using GitHub issues
1. Make changes to the repository by forking the main repository, updating your fork, and merging your changes using pull requests


## Package API specifications
#### `class yourteamrepo.Analysis(analysis_config:str)`
* Load system-wide configuration from `system_config.yml`, user configuration from `user_config.yml`, and the specified analysis configuration file
* The configuration files should include parameters for:
    * GitHub API token
    * Plot color
    * Plot title
    * Plot x and y axis titles
    * Figure size
    * Default save path

##### `load_data()`
* This function makes an HTTPS request to the GitHub API and retrieve your selected data

##### `compute_analysis() -> Any`
* This function runs an analytical measure of your choice (mean, median, linear regression, etc...)
* This function returns the data in a format of your choice

##### `plot_data(save_path:Optional[str] = None) -> matplotlib.Figure`
* *Optional* if your team only has 3 members
* This function generates a plot, display it to screen, and save it to the path in the parameter `save_path`, or the path from the configuration file if not specified
* This function returns a matplotlib Figure handle


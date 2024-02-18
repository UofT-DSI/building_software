# Building Robust Software Summative Assignment
By the end of this course, you will build an installable Python package that analyzes data retrieved from the GitHub API (or another web data provider of your choice). You'll work in teams and collaborate using tools on GitHub.

## Requirements
The deliverable, your package:
1. Must be hosted on a GitHub repository.
1. Must be installable using pip: `pip install git+https://github.com/user/yourteamrepo`
1. Must include a module named `Analysis`
1. Must include a README.md, LICENSE, and CONDUCT.md file
1. Must include unit tests, as appropriate
1. Must include a TESTS.md file detailing in point-form the non-automated tests to be performed, as appropriate
1. Must use the `logging` library to output debug, info, and error messages as appropriate
1. Must be documented using Python docstrings in the numpy style
1. Must use `try`/`except` to handle errors, must raise useful error messages, and must include at least one assertion
    * Hint: We can't analyze data that has not yet been loaded! And consider incorrect configuration parameters!

During development, your team must:
1. Track features using GitHub issues
   1. Each constituent function of the `Analysis` module should be one or more issues
   1. Each issue should be assigned to a member of your team
   1. Your team should distribute workload evenly
1. Make changes to the repository by forking the main repository, updating your fork, and merging your changes using pull requests

## Package API specifications
#### `class yourteamrepo.Analysis.Analysis(analysis_config:str)`
```
''' Load config into an Analysis object

Load system-wide configuration from `configs/system_config.yml`, user configuration from
`configs/user_config.yml`, and the specified analysis configuration file

Parameters
----------
analysis_config : str
    Path to the analysis/job-specific configuration file

Returns
-------
analysis_obj : Analysis
    Analysis object containing consolidated parameters from the configuration files

Notes
-----
The configuration files should include parameters for:
    * GitHub API token
    * ntfy.sh topic
    * Plot color
    * Plot title
    * Plot x and y axis titles
    * Figure size
    * Default save path

'''
```

##### `load_data()`
```
''' Retrieve data from the GitHub API

This function makes an HTTPS request to the GitHub API and retrieves your selected data. The data is
stored in the Analysis object.

Parameters
----------
None

Returns
-------
None

'''
```

##### `compute_analysis() -> Any`
```
'''Analyze previously-loaded data.

This function runs an analytical measure of your choice (mean, median, linear regression, etc...)
and returns the data in a format of your choice.

Parameters
----------
None

Returns
-------
analysis_output : Any

'''
```

##### `notify_done(message: str) -> None`
```
''' Notify the user that analysis is complete.

Send a notification to the user through the ntfy.sh webpush service.

Parameters
----------
message : str
  Text of the notification to send

Returns
-------
None

'''
```

##### `plot_data(save_path:Optional[str] = None) -> matplotlib.Figure`
* *Optional* if your team only has 3 members
```
''' Analyze and plot data

Generates a plot, display it to screen, and save it to the path in the parameter `save_path`, or 
the path from the configuration file if not specified.

Parameters
----------
save_path : str, optional
    Save path for the generated figure

Returns
-------
fig : matplotlib.Figure

'''
```


## Usage example
We should be able to use your package by running the following code on Colab.
``` python
!pip install git+https://github.com/user/yourteamrepo
from yourteamrepo import Analysis

analysis_obj = Analysis('config.yml')
analysis_obj.load_data()

analysis_output = analysis_obj.compute_analysis()
print(analysis_output)

analysis_figure = analysis_obj.plot_data()
```

## Assessment
You will be graded by whether you have demonstrated the following learning standards in the submitted work:
* I can interpret and write simple YAML files 
  * Demonstrated if the config files are in valid YAML
* I can load YAML files into Python
  * Demonstrated in `Analysis.__init__`
* Given documentation, I can use a Python or HTTP API
  * Demonstrated in `Analysis.load_data`
* Given a function, I can write API documentation
  * Demonstrated if your docstring is compliant with the numpy docstring specifications for the function you contributed
* Given documentation, I can write Python class and function headers described by that documentation
  * Demonstrated if the function you contributed meets the specifications above
* I can catch and handle errors using `try`/`except`
* I can write helpful error messages
* I can use the Python `logging` library to control output from my code
* I can write unit tests and integration tests using `pytest`
  * Demonstrated by associated unit tests for your designated function
* I can write a basic `pyproject.toml` configuration file for `hatchling` or `setuptools`
* I can install a package from GitHub using `pip`


## A list of other APIs you can consider
* [Pokemon data API](https://pokeapi.co/)
    * Comprehensive database of Pokemon information, abilities, etc..
* [Marvel API](https://developer.marvel.com/)
    * Retrieve information about comics, characters, events, series, etc. for all published Marvel Universe comics and movies
* [NASA Open Data API](https://api.nasa.gov/index.html)
    * Datasets from NASA missions, including near Earth object tracking, weather on Mars, etc..
* [New York Times Article Search API](https://developer.nytimes.com/docs/articlesearch-product/1/overview)
    * Trends for articles about specific topics (eg. climate change)
* [Spotify API](https://developer.spotify.com/documentation/web-api)
    * Popular artists, albums, and tracks
    * *Advanced*: Collaborations between top artists
* [OpenAI's Embeddings API](https://platform.openai.com/docs/guides/embeddings)
    * Cluster text from a book, reviews text, rule book, etc..
* [Kaggle Datasets](https://www.kaggle.com/datasets)
    * Open-source datasets on a variety of topics
    * Make sure you are pulling data live from the Kaggle API, not downloading it first

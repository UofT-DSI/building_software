import argparse
import yaml
from pprint import pprint

CONFIG_PATHS = ['system_config.yml', 'user_config.yml']

parser = argparse.ArgumentParser(description='Visualize a dataset')
parser.add_argument(
    'analysis_config',
    type=str,
    help='Path to analysis config file',
)
args = parser.parse_args()

# add the analysis config to the list of paths to load
paths = CONFIG_PATHS + [args.analysis_config]

# initialize empty dictionary to hold the configuration
config = {}

# load each config file and update the config dictionary
for path in paths:
    with open(path, 'r') as f:
        this_config = yaml.safe_load(f)
    config.update(this_config)

# print the config in an easier to read way
pprint(config)

# Using Git on Colab
## Setup
* Generate a GitHub Personal Access Token with repository access
* The token must have at least Contents and Metadata ccess




Then, run this code in a Colab cell to enable push/pull from GitHub

``` python
import os
from google.colab import userdata
token = userdata.get("ghtoken")
cmd = f'git config --global url."https://api:{token}@github.com/".insteadOf "https://github.com/"'
os.system(cmd)

```

This code will:  
* Retrieve your Personal Access Token from Colab Secrets
* Tells Git to use your token when connecting to GitHub

## Usage
Use the git command either from `getshell()` or by writing commands in a colab code shell, prefixed by `!`.

```
!git push origin main
```

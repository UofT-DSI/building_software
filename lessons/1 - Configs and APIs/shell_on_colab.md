# Using the shell in colab
Accessing the shell in Google Colab requires a little additional work.

In a new Colab notebook, run the following code:
``` python
!pip install google_colab_shell
from google_colab_shell import getshell
getshell()

```

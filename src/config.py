# RULES FOR CONFIG FILE:
# 1. If you want something from env file, put it there, and just call the os.getenv, we will load it for you.
# 2. Do not put any imports here. None but 'os'.
# 3. Only simple definitions. 
# 4. Always under $folder_of_your_project/src/config.py.


import os

NAME = "moj_ai_projekt"

# Ker želiš vse poganjati na tem istem strežniku, vpiši lokalni IP naslov (localhost)
HOSTS = [
    "127.0.0.1",
]

# Tvoj uporabnik na strežniku je 'ubuntu'
HOSTS_USER = "ubuntu"

# Standardni port za SSH je 22
HOSTS_PORT = 22

# Nastavi število procesov (GPU grafičnih kartic). Če nimaš GPU-ja, pusti 1 ali 0.
NUM_PROCESSES = 1

NAME = "moj_ai_projekt"

HOSTS = ["1.2.3.4"]
HOSTS_USER = "ubuntu"
HOSTS_PORT = 22

NUMBER_OF_PROCESSES_PER_NODE = 2

GITHUB_REPO_URL = "git@github.com:SillyusBark/moj_ai_projekt.git"

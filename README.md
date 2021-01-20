# Getting Started
1. Go to the "dependencies" file and install the dependencies listed.
2. Install Ganache -> https://www.trufflesuite.com/ganache
3. Start ganache. 
    1. Ganache usually runs on HTTP://127.0.0.1:7545. If its running on a different port, then you'll have to go into DesktopClient.py and change the parameter for the web3 instance.
4. In Pycharm, add a run configuration. 
    1. Script Path: /path/to/script/Metallic Desktop/Gui/DesktopClient.py
    2. Parameters: -d
    3. Working Directory: /path/to/directory/Metallic Desktop
    4. Make sure "Add content roots to PYTHON PATH" and "Add source roots to PYTHON PATH" are checked.
5. Click the green start arrow.
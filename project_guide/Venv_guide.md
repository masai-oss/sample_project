## Virtual Environment Setup

Virtual environments are independent groups of Python libraries, one for each project. Packages installed for one project will not affect other projects or the operating system’s packages.

Python 3 comes bundled with the venv module to create virtual environments.

## Install pyenv

To manage multiple versions of python the most popular app is pyenv:

#### Install dependencies

```bash
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
```

#### Install pyenv

1. `curl https://pyenv.run | bash`

   you should see a message like

```shell
WARNING: seems you still have not added 'pyenv' to the load path.

# Load pyenv automatically by adding
# the following to ~/.bashrc:

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

	2. `nano ~/.bashrc`
 	3. paste the message into the file
 	4. restart the shell

P.S if you're using other shell like `zsh` replace the `bash` and `bashrc` accordingly

#### Install python version 

`pyenv install <version>`

The new python version should be installed in the directory `~/.pyenv/versions/<version>`

## Create an environment
One of the most popular virtual environment manager is `virtualenv`

### Install `virtualenv`

##### Install pip

```shell
sudo apt-get install python3-pip
```

##### Install `virtualenv ` using `pip3`

`sudo pip3 install virtualenv`

##### Create virtual environment

1. It's recommended to create the virtual environment in their respective folder

2. `virtualenv -p <python file location> <virtual environment name>`

    ex:

   ​	`virtualenv -p ~/.pyenv/versions/3.7.3/bin/python venv`

##### Activate the environment
Before you work on your project, activate the corresponding environment:

```shell
source venv/bin/activate
```
Your terminal will change to show the name of the activated environment.

##### Deactivate the environment

`deactivate`

### Create `requirements.txt`

You need `requirements.txt` file to keep track of all the installed packages in your app to create it, follow the following steps

1. activate the virtual environment
2. `pip freeze` This command shows you all the packages in your virtual environment
3. `pip freeze > requirements.txt`redirects all the package names with their versions into the `requirements.txt` file
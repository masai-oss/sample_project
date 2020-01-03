## Virtual Environment Setup

Virtual environments are independent groups of Python libraries, one for each project. Packages installed for one project will not affect other projects or the operating system’s packages.

Python 3 comes bundled with the venv module to create virtual environments.

## Create an environment
Create a project folder and a venv folder within.

```
mkdir <myproject>
cd <myproject>
python3 -m venv venv
```

### Activate the environment
Before you work on your project, activate the corresponding environment:

```
source venv/bin/activate
```
Your terminal will change to show the name of the activated environment.
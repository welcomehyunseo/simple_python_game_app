# Simple Python Game App

This is skeleton project to make simple 2D game application in Python.

## Convections

### Setup
This means you are setting up everything you need to get the software running on your computer so you can continue developing and testing it.
Just follow the steps below:

* Clone Repository
* Install Python on Windows
* Create Virtual Environment & Activate
* Install Setuptools
* Install Project as an Package in development mode

#### Clone Repository

```bash
C:\...\simple_python_game_app>git clone <repo> .
```

or

```bash
C:\...\python_projects>git clone <repo>
```

#### Install Python on Windows
Visit the [Python Downloads](https://www.python.org/downloads/) page, download Python with the version specified in the 'setup.py' file, and proceed with the installation.
It must be downloaded with the version of Python specified.

```bash
C:\...\simple_python_game_app>python --version
Python 3.12.2
```

If you have multiple versions of Python installed, make sure to enter the path to the command directly, not python, as shown below.

``` bash
C:\...\simple_python_game_app>"C:\...\Python312\python.exe" --version
Python 3.12.2
```

#### Create Virtual Environment & Activate

Creating of virtual environment in done by executing the command venv.
You will need to check your Python version.

```bash
C:\...\simple_python_game_app>python -m venv .venv

```

A virtual environment will be activated using a script in its binary directory '.venv'. The invocation of the activation script is platform-specific.

| Platform    | Shell          | Command to activate                 |
| ----------- | -------------- | ----------------------------------- | 
| Windows     | cmd.exe        |  C:\\...>.venv\Scripts\activate.bat |

```bash
C:\...\simple_python_game_app>.venv\Scripts\activate

(.venv) C:\...\simple_python_game_app>
```

From now, All development activities do with the virtual environment.

#### Install Setuptools
Setuptools is a package development process library designed to facilitate packaging Python projects.

```bash
(.venv) C:\...\simple_python_game_app>python -m pip install setuptools==X.Y
```

The version X.Y is specified in the 'setup.py', like 39.1

#### Install Project as Package in development mode

Setuptools allows you to install a package without copying any files to your interpreter directory (e.g. the site-packages directory). 
This allows you to modify your source code and have the changes take effect without you having to rebuild and reinstall. 
Here’s how to do it:

```bash
(.venv) C:\...\simple_python_game_app>python -m pip install -e .
```

### Uninstall Dependencies

Dependencies 란 해당 프로젝트의 패키지를 빌드할때 같이 사용되어야 하는 다른 외부의 Packages 를 말함. (install_requires 에 명시되어 있는 packages 임.)
어떤 패키지를 사용안할때는 무조건 pip uninstall 을 이용해서 지우고 setup.py 에 있는 install_requires 목록에서 삭해하여 수정해야됨. 
왜냐하면 사용 안하는 패키지를 그대로 놨둘경우 실수로 setup.py에 명시하지 않았는데 사용할 여지가 있음.

### Version Control

Dependencies의 버전은 X.Y 로만 명시해야됨. 
기존의 Major 버전이 넘어가는 버전을 사용하는 것을 방지하고자 "pygame>=2.5,<3" 와 같이 명시해야됨.

해당 프로젝트의 버전은 1.0.0 부터 시작함.
프로젝트의 버전 관리는 Semantic Versioning 2.0.0 를 따름.

파이썬의 버전 명시가 있습니다.
이 또한 Major 버전이 바뀐다면 호환성이 망가지기 때문에 Major 버전이 바뀌지 않도록 범위를 python_requires=">=3.12,<4" 와 같이 명시해야합니다.

### Data Types
시스템은 64비트 이기 때문에 
number 는 64비트
floating point number 은 32비트 (64비트 시스템에서는 float 과 double 의 속도 차이가 없음)

## TODO

* 시스템이 64비트 인지 확인하는 코드를 심어야됨.

## Done
* setup.py 에 설정되지 않는 라이브러리를 사용해도 별다른 오류가 없음. 
    * Convention 을 정해서 해결
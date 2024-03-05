import sys
import json
import typing
import site
import pkgutil
import platform
import importlib.metadata  as implm
from enum import Enum

# TODO: refactoring
Uint = int
Int = int
Float = float
String = str

List = list
Tuple = tuple

Version = Tuple[Uint, Uint, Uint]
Json = any  # TODO: refactoring

class PackageInfo:
    def __init__(self, name: String, version: Version) -> None:
        assert String != ''

        self.name = name
        self.version = version

    def __repr__(self) -> String:
        return f"{self.__class__.__name__}" \
               f"(name={self.name}, " \
               f"version={version})"

class ComparisonOperator(Enum):
    LessThan = '<'
    GreaterThan = '>'
    LessThanOrEqualTo = '<='
    GreaterThanOrEqualTo = '<='
    EqualTo = '=='
    NotEqualTo = '!='

class VersionConstraint:
    def __init__(self, version: Version, op: ComparisonOperator) -> None:
        self.version = version
        self.op = op

# TODO: static method of String to Dependency

class Dependency:
    def __init__(
        self, 
        name: String, 
        range: List[VersionConstraint],
        ) -> None:
        assert name != ''

        self.name = name
        self.range = range

def parse_version_str(version_str: String) -> Version:
    assert version_str != ''

    arr = version_str.split('.')
    # print(arr)

    len1 = len(arr)
    assert len1 > 0
    assert len1 <= 3

    major = 0
    minor = 0
    patch = 0
    
    try:
        if len1 >= 1:
            major = Uint(arr[0])
        if len1 >= 2:
            minor = Uint(arr[1])
        if len1 >= 3:
            patch = Uint(arr[2])
    except ValueError:
        assert False

    version = (major, minor, patch)
    # print(type(version))
    return version

PY_VERSION_STR = platform.python_version()
PY_VERSION = parse_version_str(PY_VERSION_STR)
# print(PY_VERSION)
# print(type(PY_VERSION))

def is_py_version_at_least(version: Version) -> bool:

    if PY_VERSION[0] > version[0]:
        return True
    elif PY_VERSION[0] < version[0]:
        return False

    assert PY_VERSION[0] == version[0]

    if PY_VERSION[1] > version[1]:
        return True
    elif PY_VERSION[1] < version[1]:
        return False

    assert PY_VERSION[1] == version[1]

    if PY_VERSION[2] > version[2]:
        return True
    elif PY_VERSION[2] < version[2]:
        return False

    assert PY_VERSION[2] == version[2]

    return True

def in_venv() -> bool:
    # https://docs.python.org/3/library/sys.html#sys.base_prefix
    assert is_py_version_at_least([3,3,0]) == True
    # print(sys.prefix)
    # print(sys.base_prefix)
    return sys.prefix != sys.base_prefix

def read_project_json() -> Json:
    with open('project.json') as file:
        project_json = json.load(file)
        
        return project_json

    assert False

if __name__ == '__main__':
    assert in_venv() == True
    
    project_json = read_project_json()
    # print(type(project_json))
    # print(project_json)

    # print(sys.version)

    pkg_infos: List[PackageInfo] = []

    # https://docs.python.org/3/library/pkgutil.html#pkgutil.iter_modules
    assert is_py_version_at_least([3,3,0]) == True
    # https://docs.python.org/3/library/site.html#site.getsitepackages
    assert is_py_version_at_least([3,2,0]) == True
    for module_info in pkgutil.iter_modules(path=site.getsitepackages()):
        if module_info.ispkg == False:
            continue
        
        name = module_info.name

        # TODO: refactoring
        if (
            name == '_distutils_hack' or
            name == 'pip' or
            name == 'pkg_resources'
        ):
            continue

        # print(name)

        version_str = implm.version(name)
        version = parse_version_str(version_str)
        # print(version)
        
        pkg_info = PackageInfo(name, version)
        pkg_infos.append(pkg_info)
        
    # print(pkg_infos)
    
    requirements: List[String] = project_json['requirements']





    
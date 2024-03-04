import sys

# 개발할 때만 사용하는 파이썬 애플리케이션

# commands
#   setup
#   add
#   remove

# setuptools 가 설치되어 있는지 버전 상관없이. 버전체크는 setuptools 가 알아서

def in_venv():
    return sys.prefix != sys.base_prefix

if __name__ == "__main__":
    assert in_venv() == True
    
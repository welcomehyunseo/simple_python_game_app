# Simple Python Game App

## project.py

### Run
실행하는 방법
project.json 에 작성된 정보를 바탕으로 등록되지 않는 dependency 사용시 에러 발생.

### Prune
This command removes "extraneous" packages.

### Install
dependency 설치
자동으로 project.json 업데이트함.

### Uninstall
dependency 삭제
자동으로 project.json 업데이트함.

## project.json

프로젝트의 모든 정보는 project.json 파일에 작성합니다.
문자열으로 작성할 때는 공백을 포함하면 안됩니다.

### Fields

* name
* version
* requirments

#### name
문자열로 작성

#### version 
문자열로 작성
1.0.0 부터 시작함.
Semantic Versioning 2.0.0 를 따름.

#### requirments
문자열의 배열로 작성
파이썬 및 필요한 패키지의 이름을 작성합니다.

### Version Specifier
This allow manually specifying a version range or an exact version to depend on.
버전 제약은 requirments 에 작성된 이름들의 오른쪽에 추가하는 것으로써 굳이 작성하지 않아도 됩니다.
버전 제약을 콤마로 구분하여 제한없이 추가할 수 있습니다.

Here are some examples of requirements:
```text
"python>=3.2.0"
"python>2"
"python<3"
"python!=2.3"
"python==3.1"
"python>=3.2.0,<4"
```

## TODO
* 설치된 패키지의 dependencies를 체크하여 알맞은 버전을 찾아서 설치 및 조정. 한 가상 환경에서는 동일한 이름의 개별 버전의 패키지를 설치를 못하기에 패키지들과 해당 프로젝트의 dependencies 를 체크할 기능이 필요함.
# Project : Board Maestro

* 칠판 앞에서 수식을 쓰는 모션을 취할 때, 수식을 인식하여 계산해주는 시스템
* 실시간 영상처리로 얻은 자세에 대한 영상정보로부터 수식에 대한 결과를 계산하여 보여주는 것이 최종 목표입니다.

## High Level Design

![image](https://github.com/roby238/BoardMaestro/assets/45201672/aaeefcd4-a364-4b70-9625-3cac775e5cc1)

## Clone code

* (각 팀에서 프로젝트를 위해 생성한 repository에 대한 code clone 방법에 대해서 기술)

```shell
git clone https://github.com/xxx/yyy/zzz
```

## Prerequite

* (프로잭트를 실행하기 위해 필요한 dependencies 및 configuration들이 있다면, 설치 및 설정 방법에 대해 기술)

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Steps to build

* (프로젝트를 실행을 위해 빌드 절차 기술)

```shell
cd ~/xxxx
source .venv/bin/activate

make
make install
```

## Steps to run

* (프로젝트 실행방법에 대해서 기술, 특별한 사용방법이 있다면 같이 기술)

```shell
cd ~/xxxx
source .venv/bin/activate

cd /path/to/repo/xxx/
python demo.py -i xxx -m yyy -d zzz
```

## Output

* (프로젝트 실행 화면 캡쳐)

![./result.jpg](./result.jpg)

## PR rules
- part, milestone, details 포함하여 PR
  * Title :
  ```
  [<your part name>] 해당 milestone 참조
  ```
  * Description :
  ```
  details:
  
  1. 항목1
  2. 항목2
  3. 항목3
  ```
## Commit rules
- commit message: 
  ```
  git commit -m "updated code.abc by <your id>"
  ```

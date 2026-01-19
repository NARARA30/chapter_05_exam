# 라이브러리 불러오기 - import
## 해당 프로그램에서 사용하길 원하는 라이브러리를 'import'로 불러옴
## 파이썬 인터프리터에게 특정 라이브러리의 코드를 현재의 '네임스페이스'로 가져오라는 지시
import math

#라이브러리. 함수  
## 점 연산자 : 객체의 속성이나 메서드에 접근할 때 사용
math.sqrt(9)


#LEGB 규칙
## 파이썬이 이름(변수, 함수 등)을 검색할 때 참조하는 순서
## 현재의 네임스페이스(함수 내부일 경우 로컬 네임스페이스)에서 시작하여, 찾지 못하면 차례대로 외부 네임스페이스를 검색

x = '글로벌 x'

def test():
    x = '로컬 x'
    print(x)

test()
print(x)


#라이브러리에서 특정 함수/ 클래스/ 상수 불러오기

# math 라이브러리에서 sqrt 함수만 import
from math import sqrt
# sqrt 함수 사용하기(제곱근 계산)
sqrt(9)


# math 라이브러리에서 sqrt, pow, fabs 함수 import
from math import sqrt, pow, fabs

# sqrt, pow, fabs 함수 사용하기
sqrt_result = sqrt(9)
pow_result = pow(9, 2)
fabs_result = fabs(-9)


#상수
# 상수란 변하지 않는 값, 고정된 값으 가지며, 실행 중에 변경될 수 없음
# 라이브러리에서 유용하게 사용할 수 있는 여러 상수를 제공함
# 고정된 값을 직접 하드코딩하는 대신 의미 있는 이름(상수)을 통해 참조함으로써 코드의 가독성과 유지보수성을 향상시킴
from math import pi

radius = 5
circumference = 2 * pi * radius
print(f'원의 반지름이 (radius)일 때, 원의 둘레는 (circumference)입니다.')


# alias(as) 별칭을 의미
# numpy : np, pandas : pd, matplotlib.pyplot : plt, seaborn : sns, tensorflow : tf, streamlit : st
import 라이브러리 as 별칭

import pandas as pd
pd.read_csv('data.csv')

#라이브러리 확인하기
## 해당 라이브러리 버전 확인하기
## dir()함수를 사용한 속성 및 메서드 확인

#파이썬 인터프리터
import library_name
print(library_name.__version__)

#프로그램
import pkg_resources
pkg_resources.get_distribution('library_name').version

#pip 활용
## 버전 정보 뿐 아니라, 공식 홈페이지, license, 설치 위치, 위존성 정보 등의 해당 라이브러리의 개괄적인 정보 확인 가능

pip show library_name

#라이브러리 정보를 확인하는 또 다른 방법
## 파이썬 내장 함수인 help()혹은 내장 기능인 pydoc를 활용하여 해당 라이브러리의 정보 확인 가능

import pandas as pd

help(pd)

#내장 함수 dir()을 사용한 속성 및 메서드 확인
## 라이브러리나 모듈에 포함된 이름(함수, 클래스, 변수 등)을 리스트 형태로 확인할 수 있음
## 객체를 인자로 넘기지 않으면, 현재 지역 범위에서 사용할 수 있는 이름들의 리스트를 반환

import math

print(dir(math))


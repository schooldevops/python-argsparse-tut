# Python argparse 이용하기  

- Python 프로그램을 실행할때 아규먼트를 전달하여, 프로그램을 아규먼트에 따라 조작해야할 때가 많다. 
- 아규먼트 처리를 위한 방법을 스터디 하면서 정리해보았다.
- Python은 argparse 라는 모듈을 제공하여 전달한 아규먼트를 파싱할 수 있도록 하고 있다. 

## Argument 전달 단순 예제 . 

- 우선 가장 간단한 아규먼트를 입력받는 파이썬 프로그램을 살펴보자. 

```python
import argparse

# 아규먼트 파싱 메소드 
def parsing_argument():
  parser = argparse.ArgumentParser(
    description="Super Simple Argument Parsing",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
  )

  parser.add_argument(
    'title',
    metavar='str',
    type=str,
    help='Program title'
  )

  return parser.parse_args()


def main():

  args = parsing_argument()
  print("Argument Simple Sample")
  print(f"Title : {args.title}")

if __name__ == '__main__':
  main()


```

- argparse 를 import 수행한다. 입력되는 아규먼트를 argparse 모듈을 통해서 파싱할 수 있다. 
- parsing_argument() 라는 메소드를 정의했다. 아규먼트 파싱을 수행하고 파싱된 아규먼트 결과를 반환한다. 
  - parsing_argument() 내부 내용은 차츰 알아볼 것이다. 여기서는 프로그램 마다 실행되는 부분을 메소드화 했다는 것만 확인하자.
- main() 함수는 어플리케이션을 수행할때 진입을 위한 메소드이다. 
  - parsing_argument() 메소드를 호출하여 결과로 args를 받고 있다. 
  - `print(f"Title : {args.title}")` 를 이용하여 입력받은 아규먼트를 출력한다. 
  - `f"Title : {args.title}"` f 로 시작하는 문자열은 포매팅을 수행할 수 있는 문자열이다. '{}'로 감싸고 bracelet 내부에 참조값을 입력하면 출력될때 치환된 문자열로 반환된다. 
- `if __name__ == '__main__':` 는 파이썬에서 가장 일반적으로 사용하는 구문으로, 해당 어플리케이션이 모듈로 동작할 수 있도록 해준다. 
  - python app.py 로 실행하면 __name__ 변수에 __main__ 이라는 값이 세팅된다. 그때 main() 이 실행될 수 있다. 
  - 반면 모듈로 동작하면 __name__ 값이 __main__ 이 아니므로 main 함수는 실행되지 않는다. (즉, 모듈인경우 main() 메소드가 실행되지 않는다.)
  
### 테스트 수행하기

```go
python 01.arg_sample.py hello       

Argument Simple Sample
Title : hello
```

- 아규먼트로 hello 를 전달하여 결과를 확인할 수 있다.

### 프로그램 관련 도움말

- 아규먼트가 없는경우 도움말이 노출된다. 
- 또한 help 옵션을 이용하면 프로그램을 수행하기 위한 정보를 확인할 수 있다. 

```go
python 01.arg_sample.py 

usage: 01.arg_sample.py [-h] str
01.arg_sample.py: error: the following arguments are required: str
```

- 아규먼트가 없는경우 사용법과 아규먼트 추가 하라는 내용이 출력된다. 

```go
python 01.arg_sample.py -h

usage: 01.arg_sample.py [-h] str

Super Simple Argument Parsing

positional arguments:
  str         Program title

optional arguments:
  -h, --help  show this help message and exit
```

- '-h' 옵션을 이용하여 상세 사용법을 확인할 수 있다. 
- 아규먼트가 없을때 어떻게 수행해야하는지, 전달되는 아규먼트는 무엇인지 설명하고 있다. 

## 아규먼트의 종류

- 아규먼트는 크게 3가지로 나뉜다. 위치 아규먼트, 옵션 아규먼트, 플래그 아규먼트
- 위치 아규먼트:
  - 위치 아규먼트는 일반적으로 python <program> <argument....> 의 형태로 argument에 들어가는 내용이다. 
  - 이는 프로그램 실행시 반드시 필요하며, 정의된 순서에 따라서 아규먼트가 매핑이 되어야 한다. 
- 옵션 아규먼트:
  - 옵션 아규먼트는 프로그램에 필수는 아니지만 옵션으로 수행할 수 있는 아규먼트이다. 
  - 일반적으로 python <program> <위치 아규먼트> <-옵션 옵션아규먼트> ... 의 형태로 옵션으로 아규먼트를 전달한다.
  - 옵션 아규먼트는 디폴트 값을 지정해서 옵션값이 들어오지 않는경우 처리를 프로그램 내에서 수행해 주어야한다. 
- 플래그 아규먼트:
  - 플래그 아규먼트는 boolean 으로 표현되며, 해당 아규먼트가 있으면 True, 없으면 False 가 된다. 

## 위치 아규먼트 알아보기. 

- 위치 아규먼트는 이미 보았던 Super Simple Argument 샘플과 동일하며, 사용 방법에 따라 설정을 변경하면된다.

### 기본 위치 아규먼트

- 위치 아규먼트는 등록된 순서로 매핑이 된다. 
- 위치 아규먼트를 등록할때 순서는 매우 중요하며, 순서에 해당하는 아규먼트 타입이 매우 중요하다.

```python
  parser.add_argument(
    'pos_str_01',
    metavar='str',
    type=str,
    help='Position string 01'
  )

  parser.add_argument(
    'pos_int_02',
    metavar='int',
    type=int,
    help='Position int 02'
  )


  ... 생략

  args = parsing_argument()
  print("Argument Simple Sample")
  print(f"Position String : {args.pos_str_01}")
  print(f"Position int : {args.pos_int_02}")
```

- 위와 같이 첫번째 순서는 pos_str_01, pos_int_02 순서로 들어와햐 한다. 
- 그리고 순서대로 타입이 정확히 일치 해야한다. 

#### 테스트

- 첫번째 아규먼트는 문자, 두번째는 숫자 로 입력한 결과가 출력 되었다. 
- 
```go
python 02.position_argument01.py Hello 123

Argument Simple Sample
Position String : Hello
Position int : 123
```

#### 테스트 

- 아규먼트 순서가 바뀌면 어떻게 되는지 확인해보자. 

```go
python 02.position_argument01.py 123 Hello 

usage: 02.position_argument01.py [-h] str int
02.position_argument01.py: error: argument int: invalid int value: 'Hello'
```

- 보는 바와 같이 아규먼트 순서가 잘못되면 오류가 발생한다. 

### 복수개의 동일 아규먼트 받기

- 위치 아규먼트로 전달되는 아규먼트를 복수개 받고 싶은 경우가 있다. 
- 이럴때 nargs 값을 조절하여 아규먼트의 개수를 조절할 수 있다. 

```python
  parser.add_argument(
    'pos_str_01',
    metavar='str',
    type=str,
    nargs='+',
    help='Position string 01'
  )

  parser.add_argument(
    'pos_int_02',
    metavar='int',
    type=int,
    help='Position int 02'
  )

  ... 생략

  args = parsing_argument()
  print("Argument Simple Sample")
  print(f"Position String : {args.pos_str_01}")
  print(f"Position int : {args.pos_int_02}")
```

- 보는바와 같이 이전과 동일하지만 nargs='+' 가 추가 되었다. 
- nargs 에 들어갈 수 있는 형태는 다음과 같다. 
  - '*': 0개 이상의 아규먼트 
  - '?': 0, 1개의 아규먼트 
  - '+': 1개 이상의 아규먼트 
- 문자열 아규먼트 뒤에는 숫자가 오도록 숫자형 아규먼트 pos_int_02 를 추가했다. 

### 결과 보기

```go
python 03.position_argument02.py test tet1 123

Argument Simple Sample
Position String : ['test', 'tet1']
Position int : 123
```

- 문자열은 배열로 입력을 받는다. 
- 그리고 마지막 아규먼트는 숫자를 받도록 하고 있다. 

```go
python 03.position_argument02.py test tet1 sdsdf sdfsdf sfsdf 123 234 13123

Argument Simple Sample
Position String : ['test', 'tet1', 'sdsdf', 'sdfsdf', 'sfsdf', '123', '234']
Position int : 13123
```

- 마지막 숫자 1개를 제외하고 모두 문자열 아규먼트로 받았다.

### 위치 아규먼트 WrapUp

- 위치 아규먼트는 입력되는 아규먼트의 순서가 중요하다.
- 또한 아규먼트 타입의 순서역시 매우 중요하며, 올바르게 입력되지 않은경우 오류를 표시한다. 
- 그리고 nargs 라는 아규먼트 개수 지정자를 이용하여 아규먼트 개수를 지정할 수 있다. 그리고 이 지정자에 들어올 값으로 정규표현식 '*', '?', '+'가 올 수 있음을 확인할 수 있다. 

## 옵션 아규먼트 

- 옵션 아규먼트는 일반형 (--옵션이름), 축약형 (-옵션축약단어) 를 이용하여 아규먼트를 입력 받을 수 있다. 
- 옵션은 선택사항이므로, 없는경우 디폴트 값을 설정할 수 있다. 

### 기본 옵션 아규먼트 테스트

```python
import argparse

# 아규먼트 파싱 메소드 
def parsing_argument():
  parser = argparse.ArgumentParser(
    description="Super Simple Argument Parsing",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
  )

  parser.add_argument(
    '-t',
    '--title',
    metavar='str',
    type=str,
    help='Option string title',
    default='no title'
  )

  parser.add_argument(
    '-a',
    '--age',
    metavar='int',
    type=int,
    help='Option int age',
    default=0
  )

  return parser.parse_args()


def main():

  args = parsing_argument()
  print("Argument Simple Sample")
  print(f"Option String title : {args.title}")
  print(f"Option int age : {args.age}")

if __name__ == '__main__':
  main()

```

- 기본 옵션 테스트를 위와 같이 작성하였다. 
- 코드 구성은 parsing_argument(), main() 과 같이 동일하며 아규먼트 설정에서 옵션을 받을 수 있도록 수정되었다.


```python
  parser.add_argument(
    '-t',
    '--title',
    metavar='str',
    type=str,
    help='Option string title',
    default='no title'
  )
```

- '-t', '--title' 으로 단축형, 기본형 타입으로 옵션을 지정했다. 
- metavar 를 이용하여 도움말에 표시할 타입을 지정했다. 
- type은 전달된 아규먼트를 문자열 타입으로 받겠다는 의미이다. 
- help는 도움말에 표시될 설명 문자열이다. 
- default 값으로 옵션이 지정되지 않은경우 기본적으로 세팅될 값을 나타낸다. 

- 참고: 아규먼트를 조회할때에는 옵션 기본형 이름으로 접근할 수 있다. 즉, args.title 을 통해서 아규먼트 값을 조회할 수 있다. 


```python
  parser.add_argument(
    '-a',
    '--age',
    metavar='int',
    type=int,
    help='Option int age',
    default=0
  )
```

- 숫자 아규먼트 역시 문자와 다를것은 없다. 모두 동일하게 지정할 수 있으며, 기본값으로 0을 설정했다.


###  테스트

- 이제 아규먼트 없이 어떻게 출력되는지 확인해보자. 

```go
python 04.option_argument01.py 

Argument Simple Sample
Option String title : no title
Option int age : 0
```

- 보는바와 같이 아규먼트가 없다면 기본값 default 의 값으로 대체된다. 
- 만약 기본값이 없다면 어떻게 될까? 


```python
parser.add_argument(
  '-a',
  '--age',
  metavar='int',
  type=int,
  help='Option int age'
)
```

- 위아 같이 default가 없다면 결과는 다음과 같다. 

```go
python 04.option_argument01.py
Argument Simple Sample
Option String title : no title
Option int age : None
```

- 보는바와 같이 None 으로 값이 채워져 있음을 알 수 있다. 가능하면 기본값을 설정해주자. 

### 정상 케이스 테스트하기. 

- 이제 정상적으로 옵션값을 세팅해보자. 

```go
python 04.option_argument01.py -t "Hello World" -a 22

Argument Simple Sample
Option String title : Hello World
Option int age : 22
```

- 위와 같이 정상적으로 아규먼트가 잘 출력됨을 알 수 있다. 

- 문자열에 공백이 있다면 "" 으로 묶어주자. 그렇지 않으면 아규먼트를 찾지 못한다는 오류를 볼 수 있다. 

```go
python 04.option_argument01.py -t Hello World -a 22

usage: 04.option_argument01.py [-h] [-t str] [-a int]
04.option_argument01.py: error: unrecognized arguments: World
```

### 파일 옵션 아규먼트

- 옵션 아규먼트에는 파일을 받을 수도 있다. 
- 일반적으로 파일 옵션 아규먼트는 -f, --file 을 이용하여 파일값을 받아 들이게 된다. 

```python
import argparse

# 아규먼트 파싱 메소드 
def parsing_argument():
  parser = argparse.ArgumentParser(
    description="Super Simple Argument Parsing",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
  )

  parser.add_argument(
    '-f',
    '--file',
    metavar='FILE',
    type=argparse.FileType('rt'),
    help='Option File Arguments',
    default=None
  )

  return parser.parse_args()


def main():

  args = parsing_argument()
  print("Argument Simple Sample")
  print(f"Option File Arguments : {type(args.file)}")

  for line in args.file:
      print(line)

if __name__ == '__main__':
  main()

```

- 파일 아규먼트 코드 형식은 이전과 동일하다. 
- 달라진 부분은 타입 부분에서 파일 타입을 쓰는 것이다. 


```python
 parser.add_argument(
    '-f',
    '--file',
    metavar='FILE',
    type=argparse.FileType('rt'),
    help='Option File Arguments',
    default=None
  )
```

- 옵션으로 '-f', '--file' 을 지정했다. 
- metavar는 도움말에 보여줄 형식으로 파일 타입을 의미한다. 
- type 부분은 FileType('rt') 로 지정하여 읽기 텍스트의 의미이다. 
  - r: 읽기모드
  - w: 쓰기모드
  - t: 텍스트 모드
  - b: 바이너리 모드
- rw/tb 를 조합하여 사용하면 된다. 

### 테스트

- 테스트를 위해서 sample_text.txt 를 작성하자. 내부에는 아무 문자든지 여러 라인을 입력한다. 
- 그리고 다음 명령어로 파일 인수를 전달하자. 

```go
python 05.option_argument02.py -f sample_text.txt

Argument Simple Sample
Option File Arguments : <class '_io.TextIOWrapper'>
Excepteur veniam mollit pariatur dolor nulla incididunt cupi...
... 생략
...
```

- sample_text.txt 파일을 읽어서 화면에 출력하고 있다. 

### 오류 테스트

- 아규먼트가 없다면 어떻게 될까? 

```go
python 05.option_argument02.py                   
Argument Simple Sample
Option File Arguments : <class 'NoneType'>
Traceback (most recent call last):
  File "/Users/kido/Documents/01.STUDY/PYTHON/argparse-tut/05.option_argument02.py", line 33, in <module>
    main()
  File "/Users/kido/Documents/01.STUDY/PYTHON/argparse-tut/05.option_argument02.py", line 29, in main
    for line in args.file:
TypeError: 'NoneType' object is not iterable
```

- 즉 우리는 None 으로 했기 때문에 파일을 읽을 수 없다. 그러므로 파일 내용을 읽을때 항상 검사를 해 주어야한다. 

```python
def main():

  args = parsing_argument()
  print("Argument Simple Sample")
  print(f"Option File Arguments : {type(args.file)}")

  if args.file == None:
    return

  for line in args.file:
      print(line)
```

- 간단하게 파일 아규먼트가 None 인지만 검사했고 None인경우 이후 구문을 실행하지 않고 스킵한다. 

## 플래그 아규먼트 

- 플래그 아규먼트는 True/False 를 설정하는 아규먼트이다. 
- 플래그는 특정 행동을 수행할지 여부를 지정하기 위해서 주로 사용하며 샘플은 다음과 같다. 

```python
import argparse

# 아규먼트 파싱 메소드 
def parsing_argument():
  parser = argparse.ArgumentParser(
    description="Super Simple Argument Parsing",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
  )

  parser.add_argument(
    '-o',
    '--on',
    help='Flag Argument',
    action='store_true'
  )

  return parser.parse_args()


def main():

  args = parsing_argument()
  print("Argument Simple Sample")
  print(f"Option File Arguments : {type(args.on)}")
  print(f"Option File Arguments : {args.on}")


if __name__ == '__main__':
  main()


```

- 위와 같이 플래그 아규먼트는 아규먼트 옵션에 따라서 True/False 를 설정한다. 
- action 은 아규먼트가 들어온경우 어떠한 값을 지정할지 행동을 지정한다. 
  - store_true: 플래그 아규먼트가 세팅되면 True를 저장한다. 
  - store_false: 플래그 아규먼트가 세팅되면 False를 저장한다. 
  
### 테스트하기

```go
python 06.flag_argument01.py -o

Argument Simple Sample
Option File Arguments : <class 'bool'>
Option File Arguments : True

```

- '-o' 옵션을 지정하면 True로 설정되었다. 
  
```go
python 06.flag_argument01.py   

Argument Simple Sample
Option File Arguments : <class 'bool'>
Option File Arguments : False
```

- 위와 같이 옵션이 업다면 False가 되었다. 
- 만약 action='store_false' 라고 했다면 위 예제와 반대로 처리 되었을 것이다. 

## choices 로 지정된 아규먼트만 받기

- 지금까지는 아규먼트 값을 특정 타입에 따라서 입력 받을 수 있게 했다. 
- 그러나 특정 값의 범위만을 입력해야하는 경우 choices 를 이용할 수 있다. 

```python
import argparse

# 아규먼트 파싱 메소드 
def parsing_argument():
  parser = argparse.ArgumentParser(
    description="Super Simple Argument Parsing",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
  )

  parser.add_argument(
    'name',
    metavar='name',
    type=str,
    help='Student Name'
  )

  parser.add_argument(
    'age',
    metavar='age',
    type=int,
    help='Student Age',
    choices=range(1, 100)
  )

  parser.add_argument(
    'grade',
    metavar='grade',
    type=str,
    help='Student Grade',
    choices=['A', 'B', 'C', 'D', 'F']
  )

  return parser.parse_args()


def main():

  args = parsing_argument()
  print("Argument Simple Sample")
  print(f"Option File Arguments Name: {args.name}, Age: {args.age}, Grade: {args.grade}")



if __name__ == '__main__':
  main()


```

- 코드 형식은 동일하다. 
- 학생의 이름, 나이, 등급을 입력 받으며, 나이는 1 ~ 99세까지, 등급은 A ~ F 중 하나의 값이 들어올 수 있다. 

### 테스트

```go
python 07.choose_argument01.py kido 20 A

Argument Simple Sample
Argument Simple Sample
Option File Arguments Name: kido, Age: 20, Grade: A
```

- 정상적인 값의 범위가 들어갔을때 위와 같이 원하는 결과를 얻을 수 있다. 

```go
python 07.choose_argument01.py kido 100 A

usage: 07.choose_argument01.py [-h] name age grade
07.choose_argument01.py: error: argument age: invalid choice: 100 (choose from 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99)
```

- 나이를 100으로 입력하면, 해당 범위에 속하지 못하므로 오류를 내고, 입력값의 범위를 지정하고 있다. 

```go
python 07.choose_argument01.py kido 20 K 

usage: 07.choose_argument01.py [-h] name age grade
07.choose_argument01.py: error: argument grade: invalid choice: 'K' (choose from 'A', 'B', 'C', 'D', 'F')
```

- 역시 grade도 지정된 범위의 값이 아니면 오류를 내보낸다. 

## 정확한 아규먼트 개수범위 지정하기. (커스텀 액션)

- nargs='*', '+' 를 이용하면 아규먼트를 복수개 받을 수 있다고 했다. 
- nargs=2 를 이용하면 2개의 아규먼트만을 받게 된다. 
- 특정 아규먼트를 일일이 나열하지 않고 지정된 개수 범위 (2개 ~ 4개)를 받고자 한다면 어떻게 해야할까? 
- 이때 action을 이용하여 아규먼트 개수를 한번더 검증해 주는 코드를 이용하여, 아규먼트 개수를 정확히 제어할 수 있게 된다. 
- 자세한 내용은 [Manuals](https://docs.python.org/3/library/argparse.html#action) 에서 확인하자. 

```python
import argparse

# 아규먼트 파싱 메소드 
def parsing_argument():
  parser = argparse.ArgumentParser(
    description="Super Simple Argument Parsing",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
  )

  parser.add_argument(
    'name',
    metavar='name',
    type=str,
    help='Student Name',
    nargs='+',
    action=argument_count_range(2, 4)
  )

  return parser.parse_args()

def argument_count_range(nmin, nmax):
  class RequiredLength(argparse.Action):
    def __call__(self, parser, args, values, option_string=None):
        if not nmin<=len(values)<=nmax:
            msg=f'argument "{self.dest}" requires between {nmin} and {nmax} arguments'
            raise argparse.ArgumentTypeError(msg)
        setattr(args, self.dest, values)
  return RequiredLength

def main():

  args = parsing_argument()
  print("Argument Simple Sample")
  print(f"Option File Arguments Name: {args.name}")


if __name__ == '__main__':
  main()


```

- 추가된 부분은 action=argument_count_range 를 추가했다.
- 그리고 def argument_count_range 메소드를 구현했다. 

```python
def parsing_argument():
  parser = argparse.ArgumentParser(
    description="Super Simple Argument Parsing",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
  )

  parser.add_argument(
    'name',
    metavar='name',
    type=str,
    help='Student Name',
    nargs='+',
    action=argument_count_range(2, 4)
  )

  return parser.parse_args()

def argument_count_range(nmin, nmax):
  class RequiredLength(argparse.Action):
    def __call__(self, parser, args, values, option_string=None):
        if not nmin<=len(values)<=nmax:
            msg=f'argument "{self.dest}" requires between {nmin} and {nmax} arguments'
            raise argparse.ArgumentTypeError(msg)
        setattr(args, self.dest, values)
  return RequiredLength

```

- nargs='+' 를 추가하여 1개 이상의 아규먼트를 받는것을 알 수 있다. 
- action=argument_count_range(2, 4) 메소드를 이용하여 들어온 아규먼트를 테스트한다. 
  - 아규먼트 액션은 RequiredLength 라는 클래스를 생성하고, __call__ 함수를 구현하여 action 에서 해당 함수를 호출하도록 작성하였다. 
  - 코드 내부는 아규먼트의 개수를 비교해서 범위내에 속하는지 확인하고, 속하지 않으면 ArgumentTypeError를 발생하도록 했다. 
  - 그렇지 않은경우에는 setattr 을 통해서 아규먼트를 설정하고, 결과를 반환하도록 했다. 

### 테스트

```go
python 08.args_count_argument01.py test     

Traceback (most recent call last):
  File "/Users/kido/Documents/01.STUDY/PYTHON/argparse-tut/08.args_count_argument01.py", line 38, in <module>
    main()
  File "/Users/kido/Documents/01.STUDY/PYTHON/argparse-tut/08.args_count_argument01.py", line 32, in main
    args = parsing_argument()
 ... 생략
  File "/usr/local/Cellar/python@3.9/3.9.7/Frameworks/Python.framework/Versions/3.9/lib/python3.9/argparse.py", line 1930, in take_action
    action(self, namespace, argument_values, option_string)
  File "/Users/kido/Documents/01.STUDY/PYTHON/argparse-tut/08.args_count_argument01.py", line 26, in __call__
    raise argparse.ArgumentTypeError(msg)
argparse.ArgumentTypeError: argument "name" requires between 2 and 4 arguments
```

- 아규먼트가 1개일때 우리가 지정한 아규먼트 개수 체크를 통과하지 못하고 ArgumentTypeError 를 반환하고 있다. 

```go
python 08.args_count_argument01.py test test2 tet3   

Argument Simple Sample
Option File Arguments Name: ['test', 'test2', 'tet3']
```

- 정확히 범위내에 속하면 정상적으로 결과가 출력된다. 

## WrapUp

- 지금까지 Python 에서 제공하는 아규먼트 지정 방법에 대해서 몇가지 알아 보았다. 
- 이것보다 더 많은 내용이 있지만, 위 내용만으로도 프로그램에 필요한 아규먼트를 지정하고, 검증할 수 있다. 
- 좋은 프로그램은 친절한 피드백을 주어야하고, 이러한 피드백이 일정한 형식을 지니는 것이 중요하다고 생각한다. 
- argparse는 이러한 조건을 잘 만족시켜주는 모듈인것 같다.~


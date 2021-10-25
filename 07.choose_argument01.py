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
  print("Argument Simple Sample")
  print(f"Option File Arguments Name: {args.name}, Age: {args.age}, Grade: {args.grade}")


if __name__ == '__main__':
  main()


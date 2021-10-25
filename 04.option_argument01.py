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


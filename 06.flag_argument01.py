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


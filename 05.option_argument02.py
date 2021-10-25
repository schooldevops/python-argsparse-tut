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

  if args.file == None:
    return

  for line in args.file:
      print(line)

if __name__ == '__main__':
  main()


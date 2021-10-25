import argparse

# 아규먼트 파싱 메소드 
def parsing_argument():
  parser = argparse.ArgumentParser(
    description="Super Simple Argument Parsing",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
  )

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

  return parser.parse_args()


def main():

  args = parsing_argument()
  print("Argument Simple Sample")
  print(f"Position String : {args.pos_str_01}")
  print(f"Position int : {args.pos_int_02}")

if __name__ == '__main__':
  main()


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


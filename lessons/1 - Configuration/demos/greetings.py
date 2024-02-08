import argparse

parser = argparse.ArgumentParser(description='Say hello to someone.')
parser.add_argument(
    'name',
    default='World',
    type=str,
    nargs='?',
    help='Name to greet',
)
parser.add_argument(
    '--repeat',
    '-r',
    type=int,
    default=1,
    help='Number of times to greet',
)
parser.add_argument(
    '--goodbye',
    '-g',
    action='store_true',
    help='Say goodbye instead of hello',
)

args = parser.parse_args()

if args.goodbye:
    message = 'Goodbye'
else:
    message = 'Hello'

for _ in range(args.repeat):
    print(f'{message} {args.name}!')

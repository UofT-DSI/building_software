import argparse

parser = argparse.ArgumentParser(description='Say hello to someone.')
parser.add_argument('name',
                    default='World',
                    type=str,
                    nargs='?',
                    help='Name to greet')
parser.add_argument('--repeat',
                    '-r',
                    type=int,
                    default=1,
                    help='Number of times to greet')
parser.add_argument('--goodbye',
                    '-g',
                    action='store_true',
                    help='Say goodbye instead of hello')

args = parser.parse_args()

def print_greeting(name: str, repeat: int, goodbye: bool) -> None:
    ''' Print a greeting to the console.

    Parameters
    ----------
    name : str
        The name of the person to greet.
    repeat : int
        The number of times to greet the person.
    goodbye : bool
        If True, say goodbye instead of hello.

    Returns
    -------
    None
    '''
    message = 'Goodbye' if goodbye else 'Hello'

    for _ in range(repeat):
        print(f'{message} {name}!')

print_greeting(args.name, args.repeat, args.goodbye)

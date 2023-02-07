
import sys
from echo.echo import echo, hello


def main() -> int:
    """Echo the input arguments to standard output"""
    for arg in sys.argv:
        if arg == "--hello":
            hello()
        else:
            echo(arg)
    return 0

if __name__ == '__main__':
    sys.exit(main())

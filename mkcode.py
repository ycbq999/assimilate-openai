#!/usr/bin/env python


import click
from oalib.solutions import create_code


# create a click group
@click.group()
def cli():
    """Generate code examples from commets in multiple languages"""

# create a click command
@cli.command("generate")
@click.option('--language', '-l', default='Python3', help='Language to use')
@click.argument('text')

def mkcode(text, language):
    """Generate code examples from commets in multiple languages
    
    Example:
        ./mkcode.py generate "Calculate the mean distance between an array of points" -l Python3
        
    """



    create_code(text, language)

if __name__ == '__main__':
    cli()


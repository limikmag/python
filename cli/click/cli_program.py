import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--option', default=1, help='options for creating db')
@click.option('--quick', default=1, help='options for creating db')
def initdb(option: int):
    """Initialize database"""
    if option == 1:
        print("Option 1 !")
    if option == 2:
        print("Option 2 !")
    if option == 3:
        print("Option 3 !")


@cli.command()
@click.option('--upper', 'transformation', flag_value='upper',
              default=True)
@click.option('--lower', 'transformation', flag_value='lower')
def dropdb(transformation):
    """Dropping database"""
    print("Transformation: " + transformation)


@cli.command()
@click.option('--name', prompt=True)
def prompt(name):
    """Prompting from user input"""
    print('Hello %s!' % name)


@cli.command()
@click.option('--name', prompt='Your name please')
@click.option('--password', prompt=True,
              hide_input=True, confirmation_prompt=True)
def customprompt(name: str, password: str):
    """Prompting from user input with custom prompt"""
    print(f"Hello {name} and password {password}")


@cli.command()
@click.password_option()
def password(password):
    """Subcommand for typying passwords"""
    print(f"Password - {password}")


@cli.command()
@click.option('--args', nargs=2, type=float)
def multipleargs(args):
    """Passing multiple args in one command"""
    print(args)


@cli.command()
@click.option('--message', '-m', multiple=True)
def commit(message):
    """Demonstration passing multiple messages in multiple flags"""
    print('\n'.join(message))


@cli.command()
@click.option('--hash-type', type=click.Choice(['md5', 'sha1']))
def choiceoption(hash_type):
    """Choice option"""
    print(hash_type)


if __name__ == '__main__':
    cli()

from src.parse_dir import collect_fn
import click


def register_fn(directory):
    @click.group(invoke_without_command=True)
    @click.pass_context
    def cli(ctx):
        pass

    fns = collect_fn(directory)
    for f in fns:
        f(cli)

    cli()

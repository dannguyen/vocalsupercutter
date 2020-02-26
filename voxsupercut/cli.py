import click
import voxsupercut.wrangler as wrangler
import csv
import io



# from voxsupercut.utils import hello as tkhello
# from voxsupercut.wrappers import ytdl

# DEFAULT_URL = 'https://www.youtube.com/watch?v=enJwnRjkE9g'

# def main():
#     tkhello()
#     destdir = ytdl.create_project(url=DEFAULT_URL, name='wh-commercial', projects_dir="./data/voxcut_projects")
#     print("--------")
#     print(f"Wrote to:\n{str(destdir)}")


@click.group()
def cli():
    click.echo('Hello world, just top-level cli!')

@cli.command()
def fetch():
    click.echo('Fetching')


#### wrangle stuff

@cli.group()
def wrangle():
    click.echo('Wrangling')


@wrangle.command()
@click.argument('srcpath')
def flatten_transcript(srcpath):
    click.echo(f'Flatten transcript')
    click.echo(f'Reading: {srcpath}')
    data = wrangler.flatten_transcript(srcpath)
    # convert to CSV
    outs = io.StringIO()
    cw = csv.DictWriter(outs, fieldnames=wrangler.FLAT_TRANSCRIPT_HEADERS)
    cw.writeheader()
    cw.writerows(data)

    click.echo(outs.getvalue())



if __name__ == '__main__':
    print('oops!')

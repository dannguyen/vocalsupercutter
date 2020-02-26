
from voxsupercut.utils import hello as tkhello
from voxsupercut.wrappers import ytdl

DEFAULT_URL = 'https://www.youtube.com/watch?v=enJwnRjkE9g'

def main():
    tkhello()
    destdir = ytdl.create_project(url=DEFAULT_URL, name='wh-commercial', projects_dir="./data/voxcut_projects")
    print("--------")
    print(f"Wrote to:\n{str(destdir)}")

if __name__ == '__main__':
    main()

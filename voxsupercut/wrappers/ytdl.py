from pathlib import Path
from youtube_dl import YoutubeDL as Ytdl

# https://github.com/ytdl-org/youtube-dl/blob/master/README.md#embedding-youtube-dl
DEFAULT_OUTTMPL = '{project_path}/{project_name}.%(ext)s'

DEFAULT_YTDL_POSTPROCS = {
    'subtitles': {
        'key': 'FFmpegSubtitlesConvertor',
        'format': 'srt'
    },
    'audio': {
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    },

    'video': {
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    },
}

DEFAULT_YTDL_PARAMS = {
        'allsubtitles': True,
        'format': 'best',
        'keepvideo': True,
        'writeinfojson': True,
        'writesubtitles': True,
        # 'logger': MyLogger(),
        # 'progress_hooks': [my_hook],
        'postprocessors': [DEFAULT_YTDL_POSTPROCS['subtitles'].copy()]
}



def prep_project(name, projects_dir):
    projpath = Path(projects_dir).joinpath(name)
    projpath.mkdir(exist_ok=True, parents=True)
    output_template =  DEFAULT_OUTTMPL.format(project_path=projpath, project_name=name)
    return projpath, output_template


def create_project(url, name, projects_dir):
    projpath, output_template = prep_project(name, projects_dir)
    fetch_audio(url, output_template=output_template)
    fetch_video(url, output_template=output_template)
    return projpath

def fetch_audio(url, output_template=None):
    """
    downloads audio and applies post-processing
    equivalent to:

        youtube-dl --keep-video --write-info-json \
            --all-subs --convert-subs srt --write-sub \
            --extract-audio --audio-format mp3 \
            'https://www.youtube.com/watch?v=enJwnRjkE9g' \
            --output 'ztest/myfoo.%(ext)s'

    """
    yopts = DEFAULT_YTDL_PARAMS.copy()
    if output_template:
        yopts['outtmpl'] = output_template
    yopts['postprocessors'].append(DEFAULT_YTDL_POSTPROCS['audio'].copy())
    with Ytdl(params=yopts) as ydl:
        ydl.download([url])


def fetch_video(url, output_template=None):
    """downloads video and applies post-processing

    equivalent to:

        youtube-dl --keep-video  --write-info-json \
            --all-subs --convert-subs srt --write-sub \
            --recode-video mp4 \
            'https://www.youtube.com/watch?v=enJwnRjkE9g' \
            --output 'ztest/myfoo.%(ext)s'
    """
    yopts = DEFAULT_YTDL_PARAMS.copy()
    if output_template:
        yopts['outtmpl'] = output_template
    yopts['postprocessors'].append(DEFAULT_YTDL_POSTPROCS['video'].copy())
    with Ytdl(params=yopts) as ydl:
        ydl.download([url])

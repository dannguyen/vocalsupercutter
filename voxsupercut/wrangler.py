"""
wrangler.py

a set of utilities to process data formats
"""
import json
from pathlib import Path

FLAT_TRANSCRIPT_HEADERS = ('ordinal', 'content',  'type', 'confidence',
                            'start_time', 'end_time', 'duration', 'alt_count')


def flatten_transcript(data):
    """
    Given a deserialized JSON response from AWS Transcribe, produce a flattened data structure
    amenable to making CSV

    Params:
        data::dict - deserialized response, with ['results']['items'] key
        or data::str/Path: inputfile path

    Returns: list of dicts

    [{'sequence': 2, 'content': "you're", 'confidence': '1.0', 'type': 'pronunciation',
        'start_time': 3.6, 'end_time': 3.81, 'duration': 0.21}
    ]
    """

    if type(data) is not dict:
        srcpath = Path(data)
        with open(srcpath, 'r') as src:
            data = json.load(src)


    outdata = []
    for n, item in enumerate(data['results']['items']):
        d = {'ordinal': n}
        d['type'] = item['type']

        # not all items have a time element
        if item.get('start_time'):
            d['start_time'] = float(item['start_time'])
            d['end_time'] = float(item['end_time'])
            d['duration'] = round(d['end_time'] - d['start_time'], 2)
        else:
            d['start_time'] = d['end_time'] = d['duration'] = None

        alts = sorted(item['alternatives'], key=lambda a: float(a['confidence']), reverse=True)
        d['alt_count'] = len(alts)

        w = alts[0]
        d['content'] = w['content']
        d['confidence'] = float(w['confidence'])

        outdata.append(d)

    return outdata

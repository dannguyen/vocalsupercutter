import botocore
from boto3 import client as botoclient




# https://gist.github.com/dannguyen/9b8c51f5bb853209f19f1a0f18f0f74c
# https://boto3.amazonaws.com/v1/documentation/api/1.9.42/reference/services/transcribe.html#TranscribeService.Client.start_transcription_job


TEST_PUT_STUBNAME = '.voxsupercut.writable'

DEFAULT_REGION = ''
DEFAULT_S3_BUCKET = 'danntestbucket'
DEFAULT_S3_INPUT_PATH = 'voxsupercut/transcribe-input'
DEFAULT_S3_OUTPUT_PATH = 'voxsupercut/transcribe-output'

DEFAULT_TRANSCRIBE_PARAMS = {
    'LanguageCode':'en-US',
    'MediaFormat': 'mp3',
    'Settings': {
        'ShowSpeakerLabels': True,
        'MaxSpeakerLabels': 20,
    }
}



def get_bucket_status(name):
    """
    Returns: dict
        {"exists": True/False, "accessible": True/False, "writable": True/False}
    """
    print('hi')


def is_bucket_writable(name, testkey=TEST_PUT_STUBNAME):
    """

    Returns:
        tuple: first val is True/False, second val is a dict if success else an error message string
    """
    aws = botoclient('s3')
    # attempt to put an empty test file
    try:
        resp = aws.put_object(Bucket=name, Key=testkey)
    except botocore.exceptions.ClientError as err:
        return (False, str(err))

    if resp.get('ResponseMetadata') and resp['ResponseMetadata'].get('HTTPStatusCode'):
        statuscode = resp['ResponseMetadata']['HTTPStatusCode']
        if statuscode == 200:
            return (True, resp)
        else:
            msg = f"HTTP Error; received status code of {statuscode}"
            return (False, msg)
    else:
        return (False, "Error: Did not get HTTPStatusCode")



def prepare_bucket(name):
    """
    Create a writable S3 bucket with a name of `name`. If a writable bucket already exists at that
        name, return a Bucket object.

    Params:
        :name (str) the name of the bucket

    Returns:
        :str – upon success, returns the bucket name
    """

    aws = botoclient('s3')
    try:
        aws.create_bucket(Bucket=name)
    except botocore.exceptions.ClientError as e:
        raise e





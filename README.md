# voxsupercut


## Developer notes

Install locally with:

```sh
$ pip install -e .
```

Run the CLI with:

```sh
$ voxcut
```

### Version 0.0.1

Running `voxcut` produces this output:

```
    Usage: voxcut [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
      fetch
      wrangle
```


The only command that works is "wrangle":

```sh
$ voxcut wrangle flatten-transcript \
    data/samples/transcripts/whtrump.json 
```


## Todos

- Create configuration file to specify:
    - location of AWS creds
    - S3 bucket for storing audio
    - S3 bucket for writing transcripts


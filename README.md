# `grobbed`

> Real-time early grob detector for MVL

https://user-images.githubusercontent.com/45257753/149674429-ed7e8d84-0a14-4500-a826-4bce27e0a80f.mp4

## Installation

1. clone or download this repo:
1. Download [Python][python url]. Check `python` command is callable from a
   terminal (look on how to add it to your _PATH_). Also check
   `python -m pip`.
1. Place yourself in the directory.

   ```sh
   cd grobbed
   ```

1. Install dependencies:

   ```sh
   pip install -U --user -r requirements.txt
   ```

## Usage

Place yourself in the directory and execute:

```sh
python grobbed.py
```

## Parameters

You can update parameters in the file [`config.yaml`][config path].

![config file image][config file image]

[config path]: ./config.yaml
[python url]: https://www.python.org/downloads
[config file image]: ./asset/config-screenshot.png
[demo video]: ./asset/demo.mp4

# `grobbed`

> Real-time early grob detector for MVL

https://user-images.githubusercontent.com/45257753/149675224-8be4d9da-5567-4a9e-87b6-22c9578a2bcc.mp4

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

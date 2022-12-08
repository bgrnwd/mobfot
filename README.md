# pymob

[![license](https://img.shields.io/github/license/bgrnwd/pymob.svg)](LICENSE)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
![pypi](https://img.shields.io/pypi/v/pymob?color=green)
![Python CI](https://github.com/bgrnwd/pymob/workflows/Python%20CI/badge.svg)

A Python wrapper around the unofficial [FotMob](https://www.fotmob.com/) API

## Table of Contents

- [pymob](#pymob)
  - [Table of Contents](#table-of-contents)
  - [Install](#install)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Install

```sh
pip install pymob
```

## Usage

```python
from pymob import PyMob
client = PyMob()
client.get_matches_by_date("20221205")
```

## Contributing

Feel free to [open an issue](https://github.com/bgrnwd/pymob/issues/new) or submit a pull request.

## License

[MIT](./LICENSE) © Brian Greenwood

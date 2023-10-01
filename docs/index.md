# Mobfot

An unofficial Python client for the [FotMob](https://www.fotmob.com/) API

[![license](https://img.shields.io/github/license/bgrnwd/mobfot.svg)](LICENSE)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
![pypi](https://img.shields.io/pypi/v/mobfot?color=green)
[![PyPI download month](https://img.shields.io/pypi/dm/mobfot.svg)](https://pypi.python.org/pypi/mobfot/)
![Python CI](https://github.com/bgrnwd/mobfot/workflows/Python%20CI/badge.svg)

## Install

```sh
pip install mobfot
```

## Usage

### Quick Start

```python
from mobfot import MobFot
client = MobFot()
client.get_matches_by_date("20221205")
```

## Contributing

Feel free to [open an issue](https://github.com/bgrnwd/mobfot/issues/new) or submit a pull request.

## License

[MIT](https://github.com/bgrnwd/mobfot/blob/main/LICENSE) © Brian Greenwood

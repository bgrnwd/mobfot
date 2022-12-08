# mobfot

[![license](https://img.shields.io/github/license/bgrnwd/mobfot.svg)](LICENSE)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
![pypi](https://img.shields.io/pypi/v/mobfot?color=green)
![Python CI](https://github.com/bgrnwd/mobfot/workflows/Python%20CI/badge.svg)

A Python wrapper around the unofficial [FotMob](https://www.fotmob.com/) API

## Table of Contents

- [mobfot](#mobfot)
  - [Table of Contents](#table-of-contents)
  - [Install](#install)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Install

```sh
pip install mobfot
```

## Usage

```python
from mobfot import MobFot
client = MobFot()
client.get_matches_by_date("20221205")
```

## Contributing

Feel free to [open an issue](https://github.com/bgrnwd/mobfot/issues/new) or submit a pull request.

## License

[MIT](./LICENSE) © Brian Greenwood

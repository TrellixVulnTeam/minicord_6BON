# Always remember to be in lib folder when building/testing!!!
```shell
cd lib
```
## Activate virtual envoirment
```shell
source venv/bin/activate
```
## Test
```shell
python setup.py pytest
```

## Build
```shell
python setup.py bdist_wheel
```

## Install
* Download [wheelfile](lib/dlist/minicord-0.1.0-py3-none-any.whl)
* Run this command:
```shell
pip install /path/to/wheelfile.whl
```
* Import in your project:
```python
import minicord
from minicord import myfunctions
```
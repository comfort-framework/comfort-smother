# COMFORT Smother
[![Build Status](https://travis-ci.org/comfort-framework/comfort-smother.svg?branch=master)](https://travis-ci.org/comfort-framework/comfort-smother)
[![codecov](https://codecov.io/gh/comfort-framework/comfort-smother/branch/master/graph/badge.svg)](https://codecov.io/gh/fcomfort-framework/comfort-smother)
[![BCH compliance](https://bettercodehub.com/edge/badge/comfort-framework/comfort-smother?branch=master)](https://bettercodehub.com/)


### Description
COMFORT Smother is a fork and massivly reduced version of [Smother](https://github.com/ChrisBeaumont/smother). After
the installation, it provides one plug-in for [nose](https://github.com/nose-devs/nose) and a second plugin for 
[py.test](https://github.com/pytest-dev/pytest). After you have called any of these test programs with your tests, a 
.comfortsmother file is generated, which can then be used as input for the TestCoverageLoader of the 
[COMFORT framework](https://github.com/comfort-framework/comfort). This file includes coverage information based 
on each test method that is executed.

### Build
From within the directory call
```bash
python setup.py install
```

### Test
From within the directory call
```bash
make test
```

### Use
You can just call your tests like always, but just including one/two more command line loaderOptions.
- For nose call: 
```bash
nosetests --with-comfortsmother --comfortsmother-package=<root_of_project_to_track> <path_to_tests>
```

- For pytest call: 
```bash
py.test --comfortsmother=<root_of_project_to_track> <path_to_tests>
```
# RSS to Thunderbird Convertor

Convert a CSV of RSS sources to thunderbird format.

## Requirements

* Python 3.8.2
* pip 19.2.3 or later
* pip-tools 4.5.1 or later
* Virtual Environment, e.g. [virtualenv](https://docs.python-guide.org/dev/virtualenvs/)

## Setup

1. Setup a virtual environment, such as `virtualenv` e.g.:

```bash
# Create a virtual environment
virtualenv rsstothunderbirdenv

# Activate it
source rsstothunderbirdenv/bin/activate
```

2. Install the requirements for python:

```bash
pip install -r requirements.txt
```

## Usage

> _Note: Ensure that an rss-feed-list.csv file is present in your local directory_

Run the following to execute the program:

```bash
python convert.py
```

## Developer Tools

### Managing python packages

Use [pip-tools](https://github.com/jazzband/pip-tools) to manage packages in this project. Read more about it [here](https://github.com/jazzband/pip-tools)

### Debugging

Insert a breakpoint in the application like so:

```
foo = "bar"
import ipdb ; ipdb.set_trace() <=== break point
print(foo)
```

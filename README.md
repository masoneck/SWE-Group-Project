# SWE Group Project

## Setup / Run

### Setup dev environment

- Install python3 (exact version TBD, but I used 3.10)

```bash
# Install virtualenv pip package
$ python3 -m pip install virtualenv
# Setup virtual environment
$ python3 -m venv .venv/
# Activate virtual environment (Windows)
$ .venv/Scripts/activate
# Activate virtual environment (Linux)
$ source .venv/bin/activate
# Install dependences
$ python3 -m pip install -r requirements.txt
```

To leave virtual env, run: `deactivate`

## Run tests / pylint

Runs the tests located in `tests/` and can specify a specific folder to test (ex. `tests/model`).

NOTE: If another package is added, include `__init__.py` in the directory.

```bash
# defaults to run 'model', 'view', and 'controller' test packages
python3 run_tests.py [packages]
```

Run `pylint` before every commit to keep code consistent and clean among the members.

```bash
python3 run_pylint.py
```

## Project Requirements

- Administrative back end
  - Allow to modify all items
  - Allow for creation of discount codes
  - Allow for creation of sales items
  - Allow to modify users
  - Show currently placed orders
  - Show history of orders
    - Sort by order date
    - Sort by customer
    - Sort by order size in dollar amount
- Create/Modify Items for Sale
  - Must include images
  - Must include price
  - Must include quantity available
  - Must allow ability to add new items  

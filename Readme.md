# Jsonplaceholder Api tests with Python

Currently the tests cover:

  - Get all users
  - Get specific user by id
  - Create new user

### Installation

This requires [Python](https://www.python.org/downloads/) to run.

Install the following libraries

```sh
$ pip install nose requests
$ pip install nap
```

### Development

Want to contribute? Great!

#### Execution

```sh
$ cd python_api_basic
$ nosetests --verbosity=2 project
```
Sample output
```sh
test_jsonplaceholder_api.test_get_all_users ... ok
test_jsonplaceholder_api.test_get_user_by_id ... ok
test_jsonplaceholder_api.test_create_new_user ... ok

----------------------------------------------------------------------
Ran 3 tests in 1.370s

OK

```

### Todos

 - Add more tests

License
----

MIT

**Free Software, Hell Yeah!**

 


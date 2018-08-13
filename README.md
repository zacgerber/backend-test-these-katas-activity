# Test These Katas
[katas.py](katas.py) includes our solution to a [previous set of katas](https://my.kenzie.academy/courses/2/assignments/853?module_item_id=992)
assessment.

Unfortunately, while we had good intentions and wrote a [test
harness](./tests), we didn't actually write any unit tests! 

## Getting Started
There are several ways to start this activity, but we suggest that you start
by running the unit tests in a separate terminal (like the one built into VS
Code) using `rerun`:

```console
foo@bar:~ $ rerun "python -m unittest discover"
```

You should see something like the following:

![failing output](./screenshots/failing.png)

Then, open up [tests/test_katas.py](./tests/test_katas.py) and start fixing those TODOs!

Once complete, you should see the following test output:

![passing output](./screenshots/passing.png)
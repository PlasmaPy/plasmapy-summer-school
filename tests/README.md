# Tests

[**testing guide**]: https://docs.plasmapy.org/en/latest/contributing/testing_guide.html
[`src/hack/formulary/frequencies.py`]: ../src/hack/formulary/frequencies.py
[`tests/formulary/test_frequencies.py`]: formulary/test_frequencies.py
[`tests`]: .
[`src/hack`]: ../src/hack
[Nox]: https://nox.thea.codes
[pytest]: https://docs.pytest.org
[running tests]: https://docs.plasmapy.org/en/latest/contributing/testing_guide.html#running-tests

> [!TIP]
> To learn more about software testing, please check out PlasmaPy's
> [**testing guide**].

The tests in this directory are written using the [pytest] framework,
with [Nox] as the test runner.

## Locating tests

The [`tests`] directory contains the tests for the `hack` Python package
in this repository. The directory structure and organization of
[`tests`] largely mirrors that of [`src/hack`], which contains the
source code. For example, the source code of `hack.formulary.frequencies`
is located at [`src/hack/formulary/frequencies.py`], while its tests are
located at [`tests/formulary/test_frequencies.py`]

## Running tests

To run tests locally, first install [Nox] and its dependencies with:

```shell
python -m pip install nox uv
```

To run all but the slowest tests, enter the top-level directory of your
clone of this repository and run:

```shell
nox
```

For more information, please see the section in the testing guide on
[running tests].

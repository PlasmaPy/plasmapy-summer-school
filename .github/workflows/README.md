# GitHub workflows

[GitHub Actions]: https://docs.github.com/en/actions
[Nox]: https://nox.thea.codes
[YAML]: https://en.wikipedia.org/wiki/YAML

The [`.github/workflows`](.) directory contains [YAML] files that
describe [GitHub Actions] workflows such as those used to perform
continuous integration tests.

Several of the workflows invoke [Nox] sessions that are defined in the
top-level [`noxfile.py`](../../noxfile.py).

Continuous integration (CI) workflows include:

 - [`ci.yml`](./ci.yml) — perform CI checks during pull requests (PRs)

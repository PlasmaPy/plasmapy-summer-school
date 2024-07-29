# Documentation directory

[**documentation guide**]: https://docs.plasmapy.org/en/latest/contributing/doc_guide.html
[Sphinx]: https://www.sphinx-doc.org
[Nox]: https://nox.thea.codes
[Read the Docs]: https://about.readthedocs.com
[reStructuredText]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-primer
[`docs`]: .
[`docs/source/conf.py`]: conf.py
[install graphviz]: https://graphviz.org/download
[install pandoc]: https://pandoc.org/installing.html

> [!TIP]
> To learn more about writing documentation, please check out the
> [**documentation guide**].

The [`docs`] directory contains the source files for the narrative
documentation. The configuration file is [`docs/source/conf.py`].

The documentation is written in [reStructuredText], built using
[Sphinx] via a [Nox] session, and hosted by [Read the Docs].

## Building documentation

> [!TIP]
> When making a pull request, the documentation can be previewed by
> clicking on *Details* next to **docs/readthedocs.org** in the
> list of checks.

Prior to building documentation locally, please install [Nox] and its
dependencies with:

```shell
python -m pip install nox uv
```

> [!NOTE]
> It may also be necessary to [install pandoc] (and possibly [install graphviz])
> if you want to build the documentation locally.

The documentation can be built by going to the top-level directory of
your clone of PlasmaPy and running:

```shell
nox -s docs
```

The documentation preview will be built in `docs/build/html` in your
local clone of this repository.

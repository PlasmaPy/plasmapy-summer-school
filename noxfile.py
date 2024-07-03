import nox

nox.options.sessions = ["tests"]
nox.options.default_venv_backend = "uv|virtualenv"


@nox.session
def tests(session):
    """Run tests with pytest."""
    session.install(".")
    session.run("pytest")


@nox.session
def docs(session):
    """Build documentation with Sphinx."""
    session.install(".")
    session.run(
        "sphinx-build",
        "docs/source",
        "docs/build/html",
        "--builder",
        "html",
    )

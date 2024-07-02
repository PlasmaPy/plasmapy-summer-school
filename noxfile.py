import nox

nox.options.sessions = ["tests"]
nox.options.default_venv_backend = "uv|virtualenv"


@nox.session
def tests(session):
    """Run tests with pytest."""
    session.install(".")
    session.run("pytest")

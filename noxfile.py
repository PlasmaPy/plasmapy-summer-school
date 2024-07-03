import nox

nox.options.sessions = ["tests"]
nox.options.default_venv_backend = "uv|virtualenv"


@nox.session
def tests(session: nox.Session) -> None:
    """Run tests with pytest."""
    session.install(".")
    session.run("pytest", *session.posargs)


@nox.session
def docs(session: nox.Session) -> None:
    """Build documentation with Sphinx."""
    session.install(".")
    session.run(
        "sphinx-build",
        "docs/source",
        "docs/build/html",
        "--builder",
        "html",
        *session.posargs,
    )


@nox.session
def build(session: nox.Session) -> None:
    """Build & verify the source distribution and wheel."""
    session.install("twine", "build")
    build_command = ("python", "-m", "build")
    session.run(*build_command, "--sdist")
    session.run(*build_command, "--wheel")
    session.run("twine", "check", "dist/*")


@nox.session
def mypy(session: nox.Session) -> None:
    """Perform static type checking with mypy."""
    MYPY_COMMAND: tuple[str, ...] = (
        "mypy",
        ".",
        "--show-error-context",
        "--show-error-code-links",
        "--pretty",
    )
    session.install(".")
    session.run(*MYPY_COMMAND, *session.posargs)

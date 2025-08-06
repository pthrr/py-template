import nox

python_versions = ["3.10", "3.11", "3.12"]


@nox.session(python=python_versions, venv_backend="uv")
def tests(session):
    """Run tests on specified Python versions."""
    session.run_always("uv", "pip", "install", ".", external=True)
    session.run(
        "pytest",
        "-v",
        "-s",
        "--tb=short",
        "--strict-markers",
        *session.posargs,
        external=True,
    )

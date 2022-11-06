# tests/test_console.py
import pytest
import click.testing

from mathsense_gcal_import import console

@pytest.fixture
def runner():
    return click.testing.CliRunner()

def test_main_succeeds(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0

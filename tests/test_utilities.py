import pytest

from twpy.utilities import get_api_token


def test_upper_to_lower(monkeypatch):
    """Set the API_TOKEN env var to assert the behavior."""
    monkeypatch.setenv("API_TOKEN", "testingtoken")

    assert get_api_token() == "testingtoken"


def test_raise_exception(monkeypatch):
    """Remove the API_TOKEN env var and assert OSError is raised."""
    monkeypatch.delenv("API_TOKEN", raising=False)

    with pytest.raises(OSError):
        _ = get_api_token()

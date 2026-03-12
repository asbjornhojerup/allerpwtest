"""Pytest configuration for Playwright tests."""
import pytest


@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Configure browser launch arguments."""
    return {
        "headless": True,
    }


def pytest_configure(config):
    """Configure pytest markers."""
    config.addinivalue_line(
        "markers", "desktop: mark test as desktop viewport test"
    )
    config.addinivalue_line(
        "markers", "mobile: mark test as mobile viewport test"
    )

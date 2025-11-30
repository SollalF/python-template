"""Smoke tests for settings module."""

from {{ cookiecutter.package_name }}.settings import Settings, settings


def test_settings_can_be_imported():
    """Test that settings can be imported."""
    assert settings is not None
    assert isinstance(settings, Settings)


def test_settings_has_debug_field():
    """Test that settings has the debug field."""
    assert hasattr(settings, "debug")
    assert isinstance(settings.debug, bool)
    # Note: debug value depends on .env file or environment variables


def test_settings_can_be_instantiated():
    """Test that Settings class can be instantiated directly."""
    test_settings = Settings()
    assert isinstance(test_settings, Settings)
    assert isinstance(test_settings.debug, bool)

"""Tests for integration."""

import traceback
from pathlib import Path


def get_fixture_path(filename: str) -> Path:
    """Get path of fixture."""
    start_path = traceback.extract_stack()[-1].filename
    return Path(start_path).parent.joinpath("fixtures", filename)

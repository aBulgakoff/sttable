import pytest

from parser import StrTableParser


@pytest.fixture()
def tf():
    return StrTableParser()

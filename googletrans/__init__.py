"""Free Google Translate API for Python. Translates totally free of charge."""

from googletrans.client import Translator
from googletrans.constants import LANGCODES, LANGUAGES  # noqa

__version__ = "3.4.0"
__all__ = ("Translator", "LANGCODES", "LANGUAGES")

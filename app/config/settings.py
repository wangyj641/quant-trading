from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
LOG_DIR = PROJECT_ROOT / "logs"

DATA_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)


from enum import Enum


class DataProviderType(str, Enum):
    YAHOO = "yahoo"
    IBKR = "ibkr"


DATA_PROVIDER = DataProviderType.YAHOO
import sys
import logging
from csv import DictReader
from pathlib import Path

logger: logging.Logger = logging.getLogger("uvicorn.error")

try:
    filepath: str = sys.argv[1]
except IndexError:
    logger.error("Usage: python main.py <filepath>")
    logger.error("No filepath to fare table provided, check path and try again.")
    sys.exit()

def _build_path(path: str) -> Path:
    return Path(path)

def _load_db(path) -> list[dict]:
    results: list[dict] = []
    po: Path = _build_path(path)
    with po.open() as F:
        dr: DictReader = DictReader(F)
        results: list[dict] = [row for row in dr]
    return results 

MAIN_DB: list[dict] = _load_db(filepath)

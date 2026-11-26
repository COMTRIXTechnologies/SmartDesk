
from pathlib import Path
import os

APP_NAME = "COMTRIX SmartDesk"
APP_VERSION = "1.0.0"

# Store application data separately from the installation folder.
APP_DATA_DIR = (
    Path(os.environ.get("LOCALAPPDATA", Path.home()))
    / "COMTRIX"
    / "SmartDesk"
)

APP_DATA_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_PATH = APP_DATA_DIR / "smartdesk.db"

DATABASE_URL = f"sqlite:///{DATABASE_PATH.as_posix()}"

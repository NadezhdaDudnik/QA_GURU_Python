import shutil

import pytest
from zipfile import ZipFile
import os

from script_os import (
    FILES_DIR,
    FILES2_DIR,
    ARCHIVE_FILE
)


@pytest.fixture(scope="function", autouse=True)
def create_ziparchive():
    if not os.path.exists(FILES2_DIR):
        os.mkdir(FILES2_DIR)
    with ZipFile(ARCHIVE_FILE, 'w') as zip_file:
        for file in os.listdir(FILES_DIR):
            zip_file.write(os.path.join(FILES_DIR, file), file)

    yield

    shutil.rmtree(FILES2_DIR)

import os.path

CURRENT_FILE = os.path.abspath(__file__)
FILES2_DIR = os.path.join(os.path.dirname(CURRENT_FILE), 'files2')
ARCHIVE_FILE = os.path.join(FILES2_DIR, 'archive.zip')
FILES_DIR = os.path.join(os.path.dirname(CURRENT_FILE), 'files')
files = ['test_task.xlsx', 'test_task.csv', 'test_task.pdf']

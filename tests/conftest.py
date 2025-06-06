import sys
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

root_dir_content = os.listdir(BASE_DIR)
PROJECT_DIR_NAME = 'yatube_api'

if (
        PROJECT_DIR_NAME not in root_dir_content
        or not os.path.isdir(os.path.join(BASE_DIR, PROJECT_DIR_NAME))
):
    assert False, (
        f'В директории `{BASE_DIR}` не найдена папка c проектом '
        f'`{PROJECT_DIR_NAME}`. Убедитесь, что у вас верная структура проекта.'
    )

MANAGE_PATH = os.path.join(BASE_DIR, PROJECT_DIR_NAME)
project_dir_content = os.listdir(MANAGE_PATH)
FILENAME = 'manage.py'

if FILENAME not in project_dir_content:
    assert False, (
        f'В директории `{MANAGE_PATH}` не найден файл `{FILENAME}`. '
        'Убедитесь, что у вас верная структура проекта.'
    )

pytest_plugins = [
    'tests.fixtures.fixture_user',
    'tests.fixtures.fixture_data',
]

# test .md
default_md = '# api_final\napi final\n'
filename = os.path.join(BASE_DIR, 'README.md')
assert os.path.exists(filename), f'В корне проекта не найден файл `README.md`.'

# Читаем и проверяем содержимое
with open(filename, 'r', errors='ignore') as f:
    file_content = f.read().strip()
    assert file_content != default_md, 'Не забудьте оформить `README.md`.'

# ScholarManage
https://scholarmanage.onrender.com
```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
pip install -r requirements.txt
```
```
python manage.py shell
```
```
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
'xxx-xxxx'
```
シークレットキーをコピーして、ScholarManageディレクトリ内で.envファイルを作成して以下を記載する。
```.env
SECRET_KEY='xxx-xxx'
SUPERUSER_NAME='admin'
SUPERUSER_EMAIL='admin@admin.com'
SUPERUSER_BIRTHDAY='1990-01-01'
SUPERUSER_PASSWORD='admin'
SUPERUSER_LIVE_WITH_FAMILY='はい'
```
```
python manage.py makemigrations
python manage.py migrate
```
```
python manage.py runserver
```

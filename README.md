# todo
Project which manages todos

# UI
[web-UI](https://github.com/publicejh/todo/wiki/web-UI)

# 기술 스택
서버: Django(used django rest framework)

프런트: Vue.js(used vuex)

# 리눅스 서버 설치 및 실행
apt-get install git-core

git clone [ ~ ]

apt-get install python3-pip

pip3 install -r requirements.txt

sudo apt install apache2

sudo cp /{project}/Frontent/dist/index.html /var/www/html/

sudo cp /{project}/Frontent/dist/static /var/www/html/

cd /{project}/Backend/

python3 manage.py migrate

python3 manage.py runserver 8000


--> localhost로 접속

** Django settings용 json파일은 깃에 올라와 있지 않다. 추후 포멧 작성할 예정

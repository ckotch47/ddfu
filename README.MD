**DNS SEEN**
# Usage
Программа предназначена для определения ip адресса домена и для нахождение его поддоменов по славарю

Программа запускается через cli и имеет следующие параметры 


| Command  | Description                                                                                                                           |
|----------|---------------------------------------------------------------------------------------------------------------------------------------|
| --host   | в параметре указывается исходные хост для сканирования                                                                                |
| -b       | в параметре ничего не передается, его наличие включает параметр для bruteforce                                                        |
| -p       | в параметре указывается путь до файла содержащий словарь поддоменов для bruteforce                                                    |
| -r       | в параметре ничего не передается, его наличие включает рекурсию для поиска сабдоменнов помагает найти домены вида dev.app.example.com |
| --port   | номер порта для атаки ддос                                                                                                            |
| -ddos    | активация простой атаки ддос по хзосту и порту                                                                                        |
| -t       | количество пользователей для атаки ддос                                                                                               |
| -admin   | активация подбора админ панелей по словарю                                                                                            |
| -timeout | задержка между запросами для подбора панелей                                                                                          |

Примеры запуска 

python main.py --host google.com                                                          

python main.py --host google.com -b -p worldlist/subdomain.txt                            

python main.py --host google.com -b -p worldlist/subdomain.txt -r                         

python main.py --host http://localhost --port 8000 -ddos -t 10                            

python main.py --host http://localhost:8093 -p 'worldlist/admin-page.txt' -admin -timeout 0.3

## for dev
git clone https://github.com/ckotch47/opeapi-scan.git

poetry install

poetry build 

poetry run ddfu

## for install package
pip install https://github.com/ckotch47/ddfu/releases/download/0.0.1/ddfu-x.x.x-py3-none-any.whl

or

pip install https://github.com/ckotch47/ddfu/releases/download/0.0.1/ddfu-x.x.x.tar.gz


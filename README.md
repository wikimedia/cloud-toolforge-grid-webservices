# grid-webservices

## Deploying

```shell
user@laptop:~$ ssh login.toolforge.org
user@tools-sgebastion-07:~$ become grid-webservices
tools.grid-webservices@tools-sgebastion-07:~$ mkdir -pv www/python
tools.grid-webservices@tools-sgebastion-07:~$ git clone https://gerrit.wikimedia.org/r/cloud/toolforge/grid-webservices.git www/python/src
tools.grid-webservices@tools-sgebastion-07:~$ webservice python3.7 shell
tools.grid-webservices@interactive:~$ python3 -m venv www/python/venv
tools.grid-webservices@interactive:~$ www/python/venv/bin/pip install --upgrade pip wheel
tools.grid-webservices@interactive:~$ www/python/venv/bin/pip install -r www/python/src/requirements.txt
tools.grid-webservices@interactive:~$ exit
tools.grid-webservices@tools-sgebastion-07:~$ www/python/src/manage.sh start
```

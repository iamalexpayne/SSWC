# Master Django Template

## Create Development Enviroment

### From the host machine to start the Vagrant enviroment:

```shell
vagrant up
vagrant ssh
```

### Inside the Vagrant enviroment:

```shell
./make-devenv
./run-server
```

### To clean a develepment enviroment:

```shell
./make-clean
```

## Common Tasks

### Create translation files (.po)

```shell
python manage.py makemessages --locale=es --no-wrap
```

### Compile translation files (.mo)

```shell
python manage.py compilemessages --locale=es
```

### Template Version:

```python
# 2017.12.02-DEA
```
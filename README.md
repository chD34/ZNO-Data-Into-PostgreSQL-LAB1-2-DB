# Інструкція

# Шляхи: при запуску обов'язково мають бути в головній директорії - docker composer + папка app,
# в яку має бути поміщено Dockerfile, main.py, requirements та csv-файли з результатами зно

Для запуску виконати наступну команду

```bach
(docker-compose build --no-cache) -and (docker-compose up -d --force-recreate)
```

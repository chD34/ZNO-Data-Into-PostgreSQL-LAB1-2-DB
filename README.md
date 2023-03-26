# Інструкція

Шляхи: при запуску обов'язково мають бути в головній директорії - docker composer + папка app,
в яку має бути поміщено Dockerfile, main.py, requirements та csv-файли з результатами зно

Файли з результатами зно мають мати початкову назву - Odata2019File.csv та Odata2021File.csv

Файли result і time містять відповідно результати роботи програми і час за який файли 
з результатами зно запишуться у таблицю zno (PostgreSQL)

Для запуску виконати наступну команду

```bach
(docker-compose build --no-cache) -and (docker-compose up -d --force-recreate)
```

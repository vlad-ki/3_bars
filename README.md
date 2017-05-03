# Ближайшие бары
Скрипт предназначен для поиска в json фалйле самого большого, самого маленького, а так же ближайшего бара по введенным координатам.
Скачать json файл можно по ссылке http://data.mos.ru/opendata/7710881420-bary

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash

$ python bars.py # possibly requires call of python3 executive instead of just python
$ python bars.py
Введите путь к файлу: /Users/user/Documents/data-2897-2016-11-23_2.json
Введите свои кординаты (долгота): 22
Введите свои кординаты (широта): 44
Самый большой бар: {
    "global_id": 169375059,
    "system_object_id": "00138530",
    "Latitude_WGS84": "55.7011146292467670",
    "ID": "00138530",
    "Name": "Спорт бар «Красная машина»",
    "IsNetObject": "нет",
    "TypeObject": "бар",
    "AdmArea": "Южный административный округ",
    "District": "Даниловский район",
    "Address": "Автозаводская улица, дом 23, строение 1",
    "PublicPhone": [
        {
            "global_object_id": 169375059.0,
            "system_object_id": "00138530 _1",
            "PublicPhone": "(905) 795-15-84",
            "global_id": 33761.0
        }
    ],
    "SeatsCount": 450,
    "SocialPrivileges": "нет",
    "Longitude_WGS84": "37.6382285008039050",
    "geoData": {
        "type": "Point",
        "coordinates": [
            37.638228501070095,
            55.70111462948684
        ]
    }
}

Самый маленький бар: {
    "global_id": 20675518,
    "system_object_id": "00107283",
    "Latitude_WGS84": "55.8461447588834330",
    "ID": "00107283",
    "Name": "БАР. СОКИ",
    "IsNetObject": "нет",
    "TypeObject": "бар",
    "AdmArea": "Северо-Западный административный округ",
    "District": "район Митино",
    "Address": "Дубравная улица, дом 34/29",
    "PublicPhone": [
        {
            "global_object_id": 20675518.0,
            "system_object_id": "00107283 _1",
            "PublicPhone": "(495) 258-94-19",
            "global_id": 22348.0
        }
    ],
    "SeatsCount": 0,
    "SocialPrivileges": "нет",
    "Longitude_WGS84": "37.3580592058223000",
    "geoData": {
        "type": "Point",
        "coordinates": [
            37.35805920566864,
            55.84614475898795
        ]
    }
}

Ближайший бар: {
    "global_id": 281494712,
    "system_object_id": "00146638",
    "Latitude_WGS84": "55.3033000000000000",
    "ID": "00146638",
    "Name": "Staropramen",
    "IsNetObject": "нет",
    "TypeObject": "бар",
    "AdmArea": "Центральный административный округ",
    "District": "Красносельский район",
    "Address": "Садовая-Спасская улица, дом 19, корпус 1",
    "PublicPhone": [
        {
            "global_object_id": 281494712.0,
            "system_object_id": "00146638 _1",
            "PublicPhone": "(985) 069-34-47",
            "global_id": 34992.0
        }
    ],
    "SeatsCount": 50,
    "SocialPrivileges": "нет",
    "Longitude_WGS84": "36.9000000000000000",
    "geoData": {
        "type": "Point",
        "coordinates": [
            36.900000000253,
            55.303299999814
        ]
    }
}
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)

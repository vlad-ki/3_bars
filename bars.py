import json
from math import sqrt
from os.path import exists


def load_data(filepath):
    if not exists(filepath):
        return None
    with open(filepath, encoding='windows-1251') as file_handler:
        json_object = json.load(file_handler, encoding='windows-1251')
        return json_object


def get_biggest_bar(data):
    get_biggest_bar = max(data, key=lambda x: x['SeatsCount'])
    return get_biggest_bar


def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda x: x['SeatsCount'])
    return smallest_bar


def get_closest_bar(data, longitude, latitude):
    closest_bar = None
    min_distance = None
    for bar in data:
        bar_latitude = bar['geoData']['coordinates'][1]
        bar_longitude = bar['geoData']['coordinates'][0]
        x2 = bar_latitude
        x1 = bar_latitude
        y2 = longitude
        y1 = bar_longitude

        current_distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        if not min_distance or current_distance < min_distance:
            min_distance = current_distance
            closest_bar = bar

    return closest_bar


if __name__ == '__main__':
    filepath = input('Введите путь к файлу: ')
    longitude = int(input('Введите свои кординаты (долгота): '))
    latitude = int(input('Введите свои кординаты (широта): '))

    json_data = load_data(filepath)

    print('Самый большой бар: {}\n'.format(json.dumps(
        get_biggest_bar(json_data), indent=4, ensure_ascii=False)))
    print('Самый маленький бар: {}\n'.format(json.dumps(
        get_smallest_bar(json_data), indent=4, ensure_ascii=False)))
    print('Ближайший бар: {}\n'.format(json.dumps(
        get_closest_bar(json_data, longitude, latitude), indent=4, ensure_ascii=False)))

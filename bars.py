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
    return max(data, key=lambda x: x['SeatsCount'])


def get_smallest_bar(data):
    return min(data, key=lambda x: x['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    def distance_calculation(bar, longitude=longitude, latitude=latitude):

        bar_latitude = bar['geoData']['coordinates'][1]
        bar_longitude = bar['geoData']['coordinates'][0]
        x2 = latitude
        x1 = bar_latitude
        y2 = longitude
        y1 = bar_longitude

        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return min(data, key=distance_calculation)


def print_result(filepath, longitude, latitude):
    json_data = load_data(filepath)

    print('Самый большой бар: {}\n'.format(json.dumps(
        get_biggest_bar(json_data), indent=4, ensure_ascii=False)))
    print('Самый маленький бар: {}\n'.format(json.dumps(
        get_smallest_bar(json_data), indent=4, ensure_ascii=False)))
    print('Ближайший бар: {}\n'.format(json.dumps(
        get_closest_bar(json_data, longitude, latitude), indent=4, ensure_ascii=False)))


def get_data():
    filepath = input('Введите путь к файлу: ')
    longitude = int(input('Введите свои кординаты (долгота): '))
    latitude = int(input('Введите свои кординаты (широта): '))

    return filepath, longitude, latitude


if __name__ == '__main__':
    users_data = get_data()
    print_result(*users_data)

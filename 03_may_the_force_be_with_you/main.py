import requests
import json


def main():
    need_info = {}
    req_starship = requests.get('https://swapi.dev/api/starships/10/')
    data = json.loads(req_starship.text)
    need_info["name_ship"] = data["name"]
    need_info["max_atmosphering_speed"] = data["max_atmosphering_speed"]
    need_info["starship_class"] = data["starship_class"]

    pilots_lst = []
    for i_pilot_api in data["pilots"]:
        pilot_info = {}
        req_pilot = requests.get(i_pilot_api)
        data = json.loads(req_pilot.text)
        pilot_info["name"] = data["name"]
        pilot_info["height"] = data["height"]
        pilot_info["mass"] = data["mass"]

        planet_api = data["homeworld"]
        req_planet = requests.get(planet_api)
        data_planet = json.loads(req_planet.text)
        pilot_info["homeworld"] = data_planet["name"]

        pilot_info["homeworld_link"] = data["homeworld"]
        pilots_lst.append(pilot_info)
    need_info["pilots"] = pilots_lst
    print(need_info)

    with open(' Millennium Falcon.json', 'w') as file:
        json.dump(need_info, file, indent=4)


if __name__ == '__main__':
    main()



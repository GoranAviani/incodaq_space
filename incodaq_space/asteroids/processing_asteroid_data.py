
def process_asteroid_info(asteroid_info):
    test = asteroid_info
    test = asteroid_info
    for date, list_of_asteroids in asteroid_info.items():
        print("############################################################3")
        print(date)
        for asteroid in list_of_asteroids['near_earth_objects']:
            print("******************************")
            print(asteroid)
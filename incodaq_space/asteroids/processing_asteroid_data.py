
def process_asteroid_info(asteroid_info):
    result = {}
    test = asteroid_info
    test = asteroid_info
    for date, list_of_asteroids in asteroid_info['near_earth_objects'].items():
        print("############################################################3")
        print(date)
        for asteroid in list_of_asteroids:
            print("******************************")
            print(asteroid)


    return result
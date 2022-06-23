def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    list_of_food = person["favourites"]["snacks"]
    for favourite in list_of_food:
        if favourite == food:
            return True
        
    return False

def add_friend(person, friend):
    person["friends"].append(friend)

def remove_friend(person, friend):
    list_of_friends = person["friends"]
    counter = 0
    for f in list_of_friends:
        if f == friend:
            person["friends"].pop(counter)
    
        counter += 1
    
def total_money(people):
    total = 0
    for person in people:
        total += person["monies"]
        
    return total

def lend_money(person_1, person_2, amount):
    person_2["monies"] += amount
    person_1["monies"] -= amount

def all_favourite_foods(people):
    list_of_whole_snacks = []
    for person in people:
        list_of_whole_snacks += person["favourites"]["snacks"]

    return list_of_whole_snacks

def find_no_friends(people):
    list_of_no_friends = []
    for person in people:
        if len(person["friends"]) == 0:
            list_of_no_friends.append(person)
    return list_of_no_friends

def unique_favourite_tv_shows(people):
    list_of_tv_shows = []
    for person in people:
        if person["favourites"]["tv_show"] not in list_of_tv_shows:
            list_of_tv_shows.append(person["favourites"]["tv_show"])
    return list_of_tv_shows





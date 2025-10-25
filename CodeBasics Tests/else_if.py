def who_is_this_house_to_starks(house: str) -> str:
    if house == "Karstark" or house == "Tully":
        family = "friend"
    elif house == "Lannister" or house == "Frey":
        family = "enemy"
    else:
        family = "neutral"
    return family

print(who_is_this_house_to_starks('Karstark'))  # => 'friend'
print(who_is_this_house_to_starks('Frey'))      # => 'enemy'
print(who_is_this_house_to_starks('Joar'))      # => 'neutral'
print(who_is_this_house_to_starks('Ivanov'))    # => 'neutral'
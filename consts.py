FILEPATH = "images/"

USERS_IMAGES = {
    (
        '9к9191', '9к9091', '9к9291', '9к9111',
        '8к1191', '8к1591', '8к1391'
    ): f"{FILEPATH}0.jpeg",
    (
        '9к9391', '9к9392', '9к9393', '9к9394',
        '9к9311', '8к2491', '8к2492', '8к2493',
    ): f"{FILEPATH}1.jpeg",
    (
        '9к9591', '9к9491', '8к3791', '8к3291',
    ):  f"{FILEPATH}2.jpeg",
    (
        '8к1111', '7к1191', '7к1591', '7к1391',
        '7к1111', '61191', '61591', '61391',
    ): f"{FILEPATH}3.jpeg",
    (
        '7к2411', '62493', '62492', '62491',
    ): f"{FILEPATH}4.jpeg",
    (
        '7к3791', '7к3291', '63791', '63291',
    ): f"{FILEPATH}5.jpeg",
}

USERS_IMAGES_FULL = {
    group: value for key, value in USERS_IMAGES.items() for group in key
}

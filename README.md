# Vk Bot with Webhooks

You can read about few features in this app [here on habr.com](https://habr.com/post/326898/) by [strorinWind](https://github.com/strorinWind/bot) 

Here is the file structure:

```bash
├── app.py
├── commands
│   ├── info.py
│   ├── __pycache__
│   │   ├── info.cpython-36.pyc
│   │   ├── test.cpython-36.pyc
│   │   └── timetable.cpython-36.pyc
│   ├── test.py
│   └── timetable.py
├── command_system.py
├── exception
│   ├── exception.py
│   ├── __init__.py
│   └── __pycache__
│       ├── exception.cpython-36.pyc
│       └── __init__.cpython-36.pyc
├── files
│   ├── artem.jpg
│   ├── rude.jpg
│   └── warm.jpg
├── messageHandler.py
├── private
│   ├── config.yaml
│   ├── __init__.py
│   ├── parse_config.py
│   └── __pycache__
│       ├── __init__.cpython-36.pyc
│       └── parse_config.cpython-36.pyc
├── __pycache__
│   ├── command_system.cpython-36.pyc
│   ├── messageHandler.cpython-36.pyc
│   ├── settings.cpython-36.pyc
│   └── vkapi.cpython-36.pyc
├── README.md
├── requirements.txt
├── settings.py
└── vkapi.py

8 directories, 29 files

```

Example of **private/config.yaml**:
```yaml
token: qbjZSM5qG6oq6CM1A7hSNqRUcUh6uQIerjt11nKRl6YwCdS8Gy4GYeiLXjCqEsNhtGJ3zDI1CoGARTyVGYKyh
confirmation_token: dzdyabxf
access_token: stepBYstep

app:
  host: 0.0.0.0
  port: 5228

```

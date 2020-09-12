# Dolores - The Discord Bot

Inspired from WestWorld - Dolores is a discord bot which can perform the following 3 commands:
1. hey
2. !google
3. !recent

# Hey
Dolores replies **hi** to command **hey**

# !google
Dolores searches for the top 5 google results and shares the link.
example- **!google virat kohli**

# !recent
Dolores returns the list of recently searched keywords. Redis is used for persistent storage of history of search commands, such that if the python django server is killed search history is maintained.

# Technologies

Dolores is built using the following stacks.

* [Python 3](https://www.python.org/download/releases/2.7.2/)
* [pip tool](https://pypi.org/project/pip/)
* [Django 2.0](https://www.djangoproject.com/download/)
* [Redis 2.3.1](https://pypi.org/project/redis/)
* [Full requirements](requirements.txt)

# Setup
1. Set up virtualenv for dolores

2. Clone the project in a folder of choice and change the env to the newly created *virtuale-env*. Then run migrations & install dependencies,
```sh
$ git clone git@github.com:jaiesh-pahlajani/discord_bot.git
$ cd discord_bot
$ workon virtual-env
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Start Redis Server
```
redis-server
```

5. Start Dolores
```
python manage.py start_dolores
```

# Deployment 

- Currently django app is deployed on heroku and redis is deployed on aws instance of redis labs
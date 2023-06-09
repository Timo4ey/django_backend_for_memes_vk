![tests](https://github.com/Timo4ey/django_backend_for_memes_vk/actions/workflows/tests.yml/badge.svg)

# Backend for memes bot from vk.com

It's backend part of [this project]()

## Using

1. Download:

```sh
git clone https://github.com/Timo4ey/django_backend_for_memes_vk.git
```

2. Create `.env` file in the root of the project

3. Build an image

```sh
make build
```

4. Run a container

```sh
make run-server
```

4. Make migrations
`make makemigrations && make migrate`

Before start to use it check DB schema:

<img src=readme_static/images/db_diagram.png width="450">

To-do list:

1. First of all add a group or bunch of groups
    - Several approaches to do it
        - use bot from this [repo]()
        - use django admin
        - send post request

        ```sh
            curl -X POST http://172.17.0.1:8000/api/v1/groups/ 
            -H 'Content-Type: application/json'
            -d '{"group_name":"group_name","group_vk_id": 12345789}'
        ```

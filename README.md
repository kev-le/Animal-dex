# CMPT 470 Project

## Get started:

### Build and run

`docker-compose build & docker-compose up`

URLs
- Development site can be accessed at 127.0.0.1:8000
- Production site can be accessed at 127.0.0.1:8080

log-in page: 127.0.0.1:8000
home page: 127.0.0.1:8000/animals/

### Develop

- To switch between development and production, edit comments in docker-compose.yml

  admin page: 127.0.0.1:8000/admin/
  Admin ID: root
  Pwd: cmpt470

## Creating data
- Warning: The script takes roughly 4-5 hours to complete

  Go to `data/code/`.
  Run `python3 animals.py` to generate csv files.
  The `data.json` file will be needed before using `download_pictures.py`. Look at how to import data.

## Importing data

See `data/code/add_animals_to_db.py`

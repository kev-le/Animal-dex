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

## Data Scraping 

  Our `data/code/animals.py` script scrapes data from wikipedia's list of birds (in Canada), dogs, and cats. Utilzing Wikipedia API, WPTools, and BeautifulSoup,
  it requests a page and grabs the summary,picture, and infobox of each animal. The data is put into a dataframe, and gets cleaned, and exported as a csv.
  The `data/code/download_pictures.py` script downloads and resizes the images. We needed the website to load faster, so we downloaded each animals' picture
  and resized them with Pillow. We were able to get 2GB worth of pictures (roughly 1300 pictures) down to 6.6MB.
  

## Creating and Importing Data
- Warning: The script takes roughly 4-5 hours to complete. However, is not necessary to do the instructions below in order to run the application as we have already done it.
            Follow the instructions below only if you would like to re-create and re-import data.
- Change directories to `/data/code/`.
- Run `python3 animals.py` to generate csv files.
- The `data.json` file will be needed before using `download_pictures.py`. 
- When the script is complete, the content of `/data/code/images` will have to be moved to `/cmpt470/animals/static/images`
- To populate the database, please see `data/code/add_animals_to_db.py`
- Using the command `python3 manage.py dumpdata > data.json` will provide the db in a json. (optional: add `--indent 2` before the `>` to make the json more readable)

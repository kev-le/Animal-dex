# CMPT 470 Project: Animal-dex

## Getting started

### Requirements

- [Python 3](https://www.python.org/downloads/)
- [Django](https://docs.djangoproject.com/en/2.2/topics/install/) 
  - `pip install Django`
- [Docker](https://docs.docker.com/install/)

### Build and run

`docker-compose build & docker-compose up`

URLs
- Development site can be accessed at http://localhost:8000
- Production site can be accessed at http://localhost:8080

Sign-in page: http://localhost:8080  
Home page: http://localhost:8080/animals/

### Changing to Development Mode

- To switch from production deployment to develop, edit the comments in docker-compose.yml. This will use Dockerfile-app for the Django web app and Dockerfile-web for the front-end web server (nginx).

  admin page: http://localhost:8080/admin/  
  Admin ID: `admin`  
  Pwd: `a11235813`

## Features:

**Lists of Animals**

List of all animals: http://localhost:8080/animals/

Animal-dex lists every cat and dog breed in existence, as well as all bird species that can be found in Canada. Each animal is searchable by name in the search bar at the top. The animals can be filtered by letter, and can also be filtered by animal type by selecting Cats, Dogs, or Birds from the Animals drop down in the navigation bar. 

**Animal Spotting**

Example: http://localhost:8080/animals/dog/alaskan-klee-kai

Click on any animal, and there will be a button at the bottom to 'Spot' it. This allows user's to track which animals they have spotted in the wild. To view the animals that you have spotted, click on your username in the top right of the website and they will be listed in your profile.

**Pets**

List of all pets: http://localhost:8080/pets/

Rate other user's pets and upload your own! Click on the 'Pets' link in the navigation bar to see a list of all user uploaded pets. Each pet can be rated by clicking on the 'Rate me!' link in the pet information card. User's can upload their own pet by going to their profile in the top right of the website and clicking 'Add a Pet'.

**User Profile**

Your profile (must be logged in): http://localhost:8080/users/profile/

A user profile is required for pet uploading and pet rating, as well as keeping track of which animals user's have spotted in the wild. 


## Data Gathering

  Our `data/code/animals.py` script scrapes data from wikipedia's list of birds (in Canada), dogs, and cats. Utilzing Wikipedia API, WPTools, and BeautifulSoup,
  it requests a page and grabs the summary,picture, and infobox of each animal. The data is put into a dataframe, and gets cleaned, and exported as a csv.
  The `data/code/download_pictures.py` script downloads and resizes the images. We needed the website to load faster, so we downloaded each animals' picture
  and resized them with Pillow. We were able to get 2GB worth of pictures (roughly 1300 pictures) down to 6.6MB.
  

### Creating and Importing Data
- Warning: The script takes roughly 4-5 hours to complete. However, is not necessary to do the instructions below in order to run the application as we have already done it.
            Follow the instructions below only if you would like to re-create and re-import data.
- Change directories to `/data/code/`.
- Run `python3 animals.py` to generate csv files.
- The `data.json` file will be needed before using `download_pictures.py`. 
- When the script is complete, the content of `/data/code/images` will have to be moved to `/cmpt470/animals/static/images`
- To populate the database, please see `data/code/add_animals_to_db.py`
- Using the command `python3 manage.py dumpdata > data.json` will provide the db in a json. (optional: add `--indent 2` before the `>` to make the json more readable)

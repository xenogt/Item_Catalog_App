# Video Game Catalog by Genres

### Assumption and Pre-requiste
- use the vagrant box provided for this course

## setup

1. cd into the /vagrant folder where the Vagrantfile is located
2. clone this project `git clone https://github.com/xenogt/Item_Catalog_App.git`
3. `vagrant up` if you do not already have this vagrant box
4. ssh into the vagrant machine, `vagrant ssh`
5. you are now inside the vagrant machine, cd into the project dir. `cd /vagrant/Item_Catalog_App`
6. run project.py to kick off the app `python project.py`
7. open browser and go to localhost:8000 to view the application

## API Endpoints

### to get a list of all game genre
go to this URL `localhost:8000/genre/JSON`
### to get a list of game item for a given game genre
go to `localhost:8000/genre/<genre_id>/game/JSON`
### to get a single game item info
go to `localhost:8000/genre/<genre_id>/game/<game_id>/JSON`

## General Usage

- without log into the application, user can only view the content
- home page has a split view, a list of pre-populated game genres on the left, and a list of latest added game items on the right.
- click on a genre or clicking on an game item will take the user to the corresponding genre view that list out all the games of the given genre.

- log into the application allows user to add new genre or game items.  user will only be able to edit/delete items that he/she created.  appropriate flash message will shown accordingly.
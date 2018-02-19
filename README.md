# Video Game Catalog by Genres

## Final Project - Linux Server Configuration

### ssh login
    user: grader (password is grader in case switch between grader user and db user (catalog))
    ip: 54.156.227.190
    port: 2200
    private key: supplied via "note to reviewer" message

### access web application
    1. access link: http://54.156.227.190.xip.io
    2. host domain address: http://ec2-54-156-227-190.compute-1.amazonaws.com
    ***Note:*** use access link to get to the application, for some reason google's auth does not allow login using the actual awes host address.

### software packages installed
    1. python
    2. apache2
    3. apache2-bin
    4. python-httplib2
    5. python-requests
    6. python-flask
    7. python-sqlachemy
    8. python 0auth2client
    9. git
    10. libapache2-mod-wsgi
    11. python-psycopg2
    12. postgresql

### configuration made
    1. set ssh port to 2200
    2. grant sudoers right to user grader
    3. firewall allow traffic on 80, 2200, 123 and 8000 (port 8000 was used for testing when deploy app manually without mod_wsgi)
    4. apache2 site-available conf file/mod_wsgi conf
    5. create the wsgi file to link up the flask application
    6. disable the default site/conf and enable the flask app site/conf
    5. postgres configuration
        1. add new user: catalog (both on the system level and database level, password for catalog user on system is "catalog")
        2. add new database: catalog
        3. grant privileges on database to user created
        4. populated initial tables with some dummy data


## General application Usage

* without log into the application, user can only view the content
* home page has a split view, a list of pre-populated game genres on the left, and a list of latest added game items on the right.
* click on a genre to go to game view for the given genre
* click on a game item in the latest game list or in any of the genre specific view takes user to the game detail view of the item clicked
* user can delete/edit a game item within the genre specific view when logged in, if user is not the owner of the item, appropriate flash message will be displayed.
* user can also delete/edit game items in detail view of single item, the edit/delete button is hidden if the user does not own the item.


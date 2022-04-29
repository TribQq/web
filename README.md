# DjWebApp
repo in progress ...


<h3>Here worked example: </h3> 
<ul>
<li>
heroku <a href="https://djwebapp.herokuapp.com/">link</a>  (first open can be slowly ~10 sec, server on sleep and activated only on request)
</li>
<li>
or hostig <a href="http://f74708i5.beget.tech/">link</a>
</li>
</ul> 


<h2>Navigation:</h2>
<ul>
<h3><li>AboutPage</li></h3>
<p>Main page "About" with some desc and site navigation, just CSS & some native JS</p>

<img src="https://raw.githubusercontent.com/TribQq/web/master/description/AboutMe.jpg">

<h3><li>AltAboutPage</li></h3>
<p>Alternate singlepage styles with track time script + some effects</p>
<img src="https://raw.githubusercontent.com/TribQq/web/master/description/altAboutMe.jpg">


<h3><li>Portfolio</li></h3>
<p>On this page I add some apps with open source</p>

<img src="https://raw.githubusercontent.com/TribQq/web/master/description/portfolio.jpg">



<h3><li>BulletinBoardApp</li></h3>
<p>Bulletin board for ad: registratin/auth, comments, sort, Bootstrap styles, etc...)<p>
<img src="https://raw.githubusercontent.com/TribQq/web/master/description/bulletin_board.jpg">

<h3><li>BookshelfApp</li></h3>
<p>Bookshelf with: "fat models style" & django & native JS & jQuery</p>
<p>Now realized: saves, notes, map, win/lose, progress tracking, key-items </p>
<p>For example added minigame "Лодочник"</p>
<img src="https://raw.githubusercontent.com/TribQq/web/master/description/book_saves_page.jpg">



<h3><li>NotesApp</li></h3>
<p>Just notes app.Create by React + synch with DjanoApi.Realized CRUD operations, sort,create/optimize title for note  </p>

<img src="https://raw.githubusercontent.com/TribQq/web/master/description/notesApp.jpg">


</ul>

<h3>An example can be seen at the  <a href="https://djwebapp.herokuapp.com/">link</a></h3>
<h3>Or load and init repo : </h3>

<p>

main dir with settings : "mysite/settings.py"

``` 
virtualenv envName -p python3.10 
source envName/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```
app 'bookshelf do autologin to 'visitor' acc, u need create this(or u can this disable middleware)
```
python manage.py createsuperuser
   >>> Username: visitor
   >>> Email address:
   >>> Password:visitor
   >>> Password (again):visitor
   >>> Bypass password validation and create user anyway? [y/N]:y
```
```
python manage.py runserver
```
=> browser
http://127.0.0.1:8000/
</p>






# DjWebApp
repo in progress ...

<h2>Here worked example <a href="https://djwebapp.herokuapp.com/">link</a></h2> (first open can be slowly ~10 sec, server on sleep and activated only on request)


<h3>In this app tech used: </h3>
<ul>
   <li>Backend: Python(django,djangoRest), PostgreSQL</li>
   <li>Frontend: HTML & CSS, Native JS, Jquery,Bootstrap, React
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

<h3><li>BulletinBoardApp</li></h3>
<p>Bulletin board for ad, registratin, comments, sort, Bootstrap styles<p>
<img src="https://raw.githubusercontent.com/TribQq/web/master/description/bulletin_board.jpg">

<h3><li>BookshelfApp</li></h3>
<p>Bookshelf with: "fat models style" & django & native JS & jQuery</p>
<p>Now realized: saves, notes, map, win/lose, progress tracking, key-items </p>
<p>For example added minigame "Лодочник"</p>
<img src="https://raw.githubusercontent.com/TribQq/web/master/description/book_saves_page.jpg">

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
python manage.py runserver
```
=> browser
</p>






========== PythonAnyWhere3 MONTHS ==========


1=Consoles(Bash)
git clone https://github.com/bjn-redoc/blog2924

2=Add a new web app						(*)
Django -> Python 3.9 -> Project Name:[something]		(1)	

3==Files (/home/bjnbjn/[something])
//del [something] in Files					(1)

4=Consoles(Bash)
mkvirtualenv --python=/usr/bin/python3.9 blog			(2) (some commands: lsvirtualenv, deactivate, workon [name_venv], rmvirtualenv [name_venv])
	(blog)$:pip install django
check file: requiredments.txt and install Packages from  PyPI(Python Package Index)
	- whitenoise==6.7.0
	- django-resized==1.0.2
	- django-recaptcha2==1.4.1		//edit ugettext_lazy -> gettext_lazy
	- django-recaptcha==4.0.0	
	- django-multi-captcha-admin==2.0.0
	- django-ckeditor-5==0.2.13
	- django-admin-honeypot-updated-2021==1.2.0

	Fast method: upload file 'packages.txt' -> pip install -r packages.txt
===========================================================================================================
5=Code:								Next Step (*) Add a new web app		  =
-> Source code: /home/.../[something]				(1)	//change [something] to blog2924  =
-> WSGI configuration file: /var/www/..._wsgi.py							  =
project_home = '/home/bjnpythonanywhere/[something]'		(1)	//change [something] to blog2924  =
os.environ['DJANGO_SETTINGS_MODULE'] = '[something].settings'	(1)	//change [something] to blog2924  =
													  =
6=Virtualenv: blog						(2)					  =		
													  =
7=Static files:                                                                                           =
URL 	Dicrectory	/home/.../[something]/static		(1)	//change [something] to blog2924  =
URL 	Dicrectory	/home/.../[something]/static		(1)	//change [something] to blog2924  =
===========================================================================================================
8=Files 
edit file in 
'/home/bjnpythonanywhere/.virtualenvs/blog/lib/python3.9/site-packages/snowpenguin/django/recaptcha2/templatetags/recaptcha2.py'
	Line 5: from django.utils.translation import ugettext_lazy as _  
	     -> from django.utils.translation import gettext_lazy as _
'/home/bjnpythonanywhere/.virtualenvs/blog/lib/python3.9/site-packages/snowpenguin/django/recaptcha2/fields.py'
	Line 7: from django.utils.translation import ugettext_lazy as _  
	     -> from django.utils.translation import gettext_lazy as _

9=Files
edit file settings.py	
ALLOWED_HOSTS = ['*'] -> ALLOWED_HOSTS = ['bjnpythonanywhere.pythonanywhere.com']	// base on your domain
TEMPLATES = [...'DIRS':['template'],...] -> EMPLATES = [...'DIRS':['/home/[something]/blog2924/template'],...]		//change [something] to [yoursite]
RECAPTCHA_PUBLIC_KEY = 'key'	//from developers.google.com/recaptcha
RECAPTCHA_PRIVATE_KEY = 'key'	//from developers.google.com/recaptcha

===Final (create your user admin login to use)
1=Consoles(Bash)
python manage.py createsuperuser


========== Migrate your date to another site==========	you can't keep your site on pythonanywhere by click 'Run until 3 months from to day' it will reset 
1 file db.sqlite3 in '/home/[yoursite]/blog2924'		//file dd.sqlite3 contains 'data' and 'account' in it 
	-> download file db.sqlite3				
2 file media in '/home/[yoursite]/blog2924'
	(venv) .../blog2924 ...$zip -medias.zip media		//zip all images to migrate to another site
	-> download file medias.zip
3 packages.txt		//pip install -r packages.txt


=== Backup Daily ===
https://www.pythonanywhere.com/forums/topic/33778/
Tasks -> Command: 	'cp /home/bjnbjn/blog2924/db.sqlite3 /home/bjnbjn/backups/mydb_$(date +%Y-%m-%dT%H:%M:%S).db' -> Create

			'find /home/limaweb/backups -name 'mydb_*.db' -type f -mtime +14'
			(This command would delete all files with filenames like mydb_*.db from /home/limaweb/backups if they were last modified more than 14 days ago.)
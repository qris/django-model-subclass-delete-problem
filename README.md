h1. Model subclass not in INSTALLED_APPS incorrectly collected during object deletion

Reproduces a [bug](https://code.djangoproject.com/ticket/19422) in
Django where you have a model that's installed (in INSTALLED_APPS), and a
subclass that's NOT installed (so it shouldn't be used), but deleting an
instance of the parent model causes a crash.

For example, if there is a Session subclass somewhere in your code, but
not in an INSTALLED_APPS models.py, then the following code will fail:

	s = Session()
	from datetime import datetime
	s.expire_date = datetime.now()
	s.save()
	s.delete()

It fails here, when trying to delete objects:

	Traceback (most recent call last):
	  File "/home/installuser/Dropbox/projects/ischool/delete_related_test/project/demo/tests.py", line 14, in test_demo
	    s.delete()
	  File "/home/installuser/Dropbox/projects/ischool/delete_related_test/ve/local/lib/python2.7/site-packages/django/db/models/base.py", line 575, in delete
	    collector.collect([self])
	  File "/home/installuser/Dropbox/projects/ischool/delete_related_test/ve/local/lib/python2.7/site-packages/django/db/models/deletion.py", line 175, in collect
	    if not sub_objs:
	  File "/home/installuser/Dropbox/projects/ischool/delete_related_test/ve/local/lib/python2.7/site-packages/django/db/models/query.py", line 130, in __nonzero__
	    iter(self).next()
	  File "/home/installuser/Dropbox/projects/ischool/delete_related_test/ve/local/lib/python2.7/site-packages/django/db/models/query.py", line 118, in _result_iter
	    self._fill_cache()
	  File "/home/installuser/Dropbox/projects/ischool/delete_related_test/ve/local/lib/python2.7/site-packages/django/db/models/query.py", line 875, in _fill_cache
	    self._result_cache.append(self._iter.next())
	  File "/home/installuser/Dropbox/projects/ischool/delete_related_test/ve/local/lib/python2.7/site-packages/django/db/models/query.py", line 291, in iterator
	    for row in compiler.results_iter():
	  File "/home/installuser/Dropbox/projects/ischool/delete_related_test/ve/local/lib/python2.7/site-packages/django/db/models/sql/compiler.py", line 763, in results_iter
	    for rows in self.execute_sql(MULTI):
	  File "/home/installuser/Dropbox/projects/ischool/delete_related_test/ve/local/lib/python2.7/site-packages/django/db/models/sql/compiler.py", line 818, in execute_sql
	    cursor.execute(sql, params)
	  File "/home/installuser/Dropbox/projects/ischool/delete_related_test/ve/local/lib/python2.7/site-packages/django/db/backends/sqlite3/base.py", line 337, in execute
	    return Database.Cursor.execute(self, query, params)
	DatabaseError: no such table: utility_sessionwithextrafield

It seems that the model was registered just by being loaded, and
associated itself with a parent model (superclass), but its database table
never got created because it wasn't in INSTALLED_APPS.

So these two should be consistent with each other: either we only register
models for INSTALLED_APPS, or we create database tables for all registered
models even if they're not in INSTALLED_APPS.


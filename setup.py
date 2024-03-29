from distutils.core import setup

setup (
    name = 'django-remember_me',
    version = '0.1.1',
    description = 'A Django application that provides a login form with a Remember Me checkbox.',
    author = 'creecode',
    author_email = 'creecode@gmail.com',
    url = 'http://code.google.com/p/django-remember-me/',
    download_url = 'http://django-remember-me.googlecode.com/files/django-remember_me-0.1.1.tar.gz',
    license = 'BSD',
    packages = [
        'remember_me',
        ],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        ],
    )

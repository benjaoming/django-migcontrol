Migration Control website
=========================

Test

This website is based on:

* Django
* Wagtail

Development
-----------

To get started, run the following commands:

.. code-block:: console

    # Create a virtualenv and activate it
    # (remember to always activate it when you run commands)
    python3 -m venv .virtualenv
    source .virtualenv/bin/activate

    # Install dependencies
    pip install -r requirements.txt

    # Run migrations (creates the SQLite development database)
    # Remember to always run this step when migrations change
    python manage.py migrate

    # Run the development webserver
    python manage.py runserver

Once the local webserver is running, you can access the website on
``http://localhost:8000``.

If you want to make usage of virtualenvs smoother, consider installing
`virtualenv-wrapper <https://virtualenvwrapper.readthedocs.io/en/latest/>`__

Development next steps
----------------------

After you have the site running, you should install
`pre-commit <https://pre-commit.com/>`__ before further changes. Once again,
make sure that your virtualenv is active and then run:

.. code-block:: console

    pip install pre-commit
    pre-commit install

Nothing will happen after this, but in the future your git commits will be
verified locally.

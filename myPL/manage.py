#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from django.db import connection

def set_test_db():
    from geronte.models import Patient
    
    #Test if the table Patient exists
    if "geronte_patient" not in connection.introspection.table_names():
        return None
    
    #Test if there is no patient in database
    if len(Patient.objects.all()) != 0:
        return None
    
    #Create first patient
    Patient.objects.create(name="John Doe", age=45)
    return None

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myPL.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    #Create first patient if not exists
    set_test_db()


if __name__ == '__main__':
    main()

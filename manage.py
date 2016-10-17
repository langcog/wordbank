#!/usr/bin/env python
import sys
print sys.path
import os
import sys
import faulthandler

if __name__ == "__main__":

    faulthandler.enable()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wordbank.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

#!/usr/bin/env python
import os
import sys

from AProject.settings import  TIME_ZONE
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AProject.settings")

    print TIME_ZONE
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

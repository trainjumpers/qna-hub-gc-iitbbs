import re

PASSWORD_REGEX = re.compile(r"[\w!@#$%&*-+(){}]+")
EMAIL_REGEX = re.compile(r"([a-zA-Z0-9_.+-]+@iitbbs.ac.in)")

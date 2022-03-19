import re

PASSWORD_REGEX = re.compile(r"[\w!@#$%&*-+(){}]+")
EMAIL_REGEX = re.compile(r"([a-zA-Z0-9_.+-]+@iitbbs.ac.in)")

VERIFICATION_EMAIL_SUBJECT = """
Hello,
Please click on this link {link} to verify your email address. This link will expire in a day.
Regards,
"""

EXPIRED_VERIFICATION_EMAIL_HTML = """
<html>
    <head>
        <title>Verify Email</title>
    </head>
    <body>
        <h2>This email verification link has expired. Please generate a new verification link.</h2>
    </body>
</html>
"""

SUCCESS_VERIFICATION_EMAIL_HTML = """
<html>
    <head>
        <title>Verify Email</title>
    </head>
    <body>
        <h3>Your email has been successfully verified.</h3>
    </body>
</html>
"""

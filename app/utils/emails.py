import os
import smtplib
import ssl
import urllib.parse

from app.utils.jwt import jwt_encode_user_to_token


def generate_email_verification_url(email: str) -> str:
    """Generates the email verification url.
    Args:
        email: email of the user to be verified.
    Returns:
        verification_url: url which when clicked, would verify the user's account on Quriate.
    """

    encoded_email: str = jwt_encode_user_to_token({"email": email})
    verification_url = f"/api/v1/accounts/verify_email/{encoded_email}"

    application_host: str = os.environ.get("APPLICATION_HOST")
    return urllib.parse.urljoin(application_host, verification_url)


def send_email(receiver_email_id: str, subject: str, message: str):
    """Sends an email via SMTP (over SSL) from the service account email address.
    Args:
        receiver_email_id: email id of the receiver.
        subject: title of the email.
        message: text content of the email.
    """

    context = ssl.create_default_context()
    service_email_id: str = os.environ.get("SERVICE_EMAIL_ID")
    service_email_password: str = os.environ.get("SERVICE_EMAIL_PASSWORD")
    email_text = f"Subject: {subject}\n{message}"
    with smtplib.SMTP_SSL("smtp.gmail.com", smtplib.SMTP_SSL_PORT, context=context) as server:
        server.login(service_email_id, service_email_password)
        server.sendmail(service_email_id, receiver_email_id, email_text)
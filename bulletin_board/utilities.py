from datetime import datetime
from os.path import splitext

from django.template.loader import render_to_string
from django.core.signing import Signer

from mysite.settings import ALLOWED_HOSTS

signer = Signer()


def send_activation_notification(user):
    """ send activation notification """
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'
    context = {'user': user, 'host': host, 'sign': signer.sign(user.username)}
    subject = render_to_string('email/activation_letter_subject.txt', context)
    body_text = render_to_string('email/activation_letter_body.txt', context)
    user.email_user(subject, body_text)


def get_timestamp_path(instance, filename):
    """ generate timestamp-name for img bb_== app + timestamp"""
    return 'bb_%s%s' % (datetime.now().timestamp(), splitext(filename)[1])


def send_new_comment_notification(comment):
    """ send new comment notification """
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'
    author = comment.bb.author
    context = {'author': author, 'host': host, 'comment': comment}
    subject = render_to_string('email/new_comment_letter_subject.txt', context)
    body_text = render_to_string('email/new_comment_letter_body.txt', context)
    author.email_user(subject, body_text)


def send_password_reset(user):
    """ send password reset"""
    if ALLOWED_HOSTS:
        host = 'http://'+ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'

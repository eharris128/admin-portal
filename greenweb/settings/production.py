from .common import * # noqa


ANYMAIL = {
    'MAILGUN_API_KEY': env('MAILGUN_API_KEY'),
}
EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
DEFAULT_FROM_EMAIL = 'hello@thegreenwebfoundation.org'
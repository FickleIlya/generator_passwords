# generator_passwords
need to create 2 files: .env_dev and .env_prod
which contains SECRET_KEY, DEBUG, ALLOWED_HOSTS, DJANGO_LOGLEVEL,
for dev DEBUG=1, ALLOWED_HOSTS=localhost 127.0.0.1, DJANGO_LOGLEVEL=info
for prod dev DEBUG=0, ALLOWED_HOSTS=<ip_or_domain_1> <ip_or_domain_2> ... , DJANGO_LOGLEVEL=info
if you wnat start server manually create .env in code/ with .env_dev values

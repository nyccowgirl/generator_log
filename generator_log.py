import itertools

# Limits timestamp to first 500 log items.

for x in (line.split('[')[1].split(']')[0] for line in itertools.islice(open('/etc/httpd/logs/access_log'), 0, 500)):
    print(x)


# With no limit

for x in (line.split('[')[1].split(']')[0] for line in open('/etc/httpd/logs/access_log')):
    print(x)

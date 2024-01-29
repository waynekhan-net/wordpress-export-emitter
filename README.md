# README

Emit a [Wordpress Export](https://wordpress.com/support/export/) input file `example.xml` as individual [Markdown](https://daringfireball.net/projects/markdown/syntax) files.

```text
# Install deps
pipenv install --python $(which python3)

# Run it
pipenv run ./main.py

# Get a shell in the virtualenv
pipenv shell

# Sonar
coverage run ./main.py && \
  coverage xml && \
  /opt/sonar-scanner/bin/sonar-scanner \
  -Dsonar.host.url=$SONAR_HOST_URL \
  -Dsonar.login=$SONAR_TOKEN \
  -X \
  > scanner.txt
```

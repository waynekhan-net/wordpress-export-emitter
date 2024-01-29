# README

Emit a [Wordpress Export](https://wordpress.com/support/export/) input file `example.xml` as individual [Markdown](https://daringfireball.net/projects/markdown/syntax) files.

```text
# Install deps
pipenv install --python $(which python3)

# Run it
pipenv run ./main.py

# Generate Coverage.py XML
pipenv shell
coverage xml

# Sonar
/opt/sonar-scanner/bin/sonar-scanner \
  -Dsonar.host.url=$SONAR_HOST_URL \
  -Dsonar.login=$SONAR_TOKEN \
  -X \
  > scanner.txt
```

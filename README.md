# README

Emit a [Wordpress Export](https://wordpress.com/support/export/) input file `example.xml` as individual [Markdown](https://daringfireball.net/projects/markdown/syntax) files.

```text
# Install deps
pipenv install --python $(which python3)

# Run it
pipenv run ./main.py

# Get a shell in the virtualenv
pipenv shell

# Sonar (coverage report; CI uploads it via the SonarQube scan action)
pipenv run coverage run ./main.py && \
  pipenv run coverage xml
```

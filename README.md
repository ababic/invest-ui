# invest-ui

[![code-climate-image]][code-climate]
[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![gemnasium-image]][gemnasium]

---

For more information on installation please check the [Developers Onboarding Checklist](https://uktrade.atlassian.net/wiki/spaces/ED/pages/32243946/Developers+onboarding+checklist)

## Requirements

[Python 3.5](https://www.python.org/downloads/release/python-350/)

[Docker >= 1.10](https://docs.docker.com/engine/installation/)

[Docker Compose >= 1.8](https://docs.docker.com/compose/install/)


## Local installation

    $ git clone https://github.com/uktrade/invest-ui
    $ cd invest-ui
    $ make

## Running with Docker
Requires all host environment variables to be set.

    $ make docker_run

### Run debug webserver in Docker

    $ brew link gettext --force (OS X only)
    $ make docker_debug

### Run tests in Docker

    $ make docker_test

### Host environment variables for docker-compose
``.env`` files will be automatically created (with ``env_writer.py`` based on ``env.json``) by ``make docker_test``, based on host environment variables with ``INVEST_UI`` prefix.

#### Web server
| Host environment variable | Docker environment variable  |
| ------------- | ------------- |
| INVEST_UI_SECRET_KEY | SECRET_KEY |
| INVEST_UI_PORT | PORT |
| INVEST_UI_API_SIGNATURE_SECRET | API_SIGNATURE_SECRET |
| INVEST_UI_API_CLIENT_BASE_URL | API_CLIENT_BASE_URL |
| INVEST_UI_COMPANIES_HOUSE_SEARCH_URL | COMPANIES_HOUSE_SEARCH_URL |
| INVEST_UI_SSO_API_CLIENT_BASE_URL | SSO_API_CLIENT_BASE_URL |
| INVEST_UI_UI_SESSION_COOKIE_SECURE | UI_SESSION_COOKIE_SECURE |

## Debugging

### Setup debug environment

    $ make debug

### Run debug webserver

    $ make debug_webserver

### Run debug tests

    $ make debug_test

## CSS development

### Requirements
[node](https://nodejs.org/en/download/)
[SASS](http://sass-lang.com/)
[gulp](https://gulpjs.com/)

	$ npm install

### Update CSS under version control

	$ gulp sass

### Rebuild the CSS files when the scss file changes

	$ gulp sass:watch

## Session

Signed cookies are used as the session backend to avoid using a database. We therefore must avoid storing non-trivial data in the session, because the browser will be exposed to the data.

## Translations

Follow the <a href="https://docs.djangoproject.com/en/1.9/topics/i18n/translation/#localization-how-to-create-language-files" target="_blank">Django documentation</a>

To create or update `.po` files:

	$ make debug_manage cmd="makemessages"

To compile `.mo` files (no need to add these to source code, as this is done automatically during build):

	$ make debug_manage cmd="compilemessages"


[code-climate-image]: https://codeclimate.com/github/uktrade/directory-ui-supplier/badges/issue_count.svg
[code-climate]: https://codeclimate.com/github/uktrade/directory-ui-supplier

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-ui-supplier/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-ui-supplier/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-ui-supplier/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-ui-supplier

[gemnasium-image]: https://gemnasium.com/badges/github.com/uktrade/directory-ui-supplier.svg
[gemnasium]: https://gemnasium.com/github.com/uktrade/directory-ui-supplier

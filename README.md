## Setup Requirements

---

- python 3.8+
  - pip3
  - virtualenv
- Visual Studio Code
- Docker
- git
- [postgresql](https://www.postgresql.org/download/)

## Repository Setup

---

To setup the virtual environment and install dependencies run

```bash
virtualenv -p python3 venv  # to be created only once
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the same folder as `.env.test`. This file will contain all the environment
variables and secrets that are loaded when the application server starts.

**NOTE** - Ensure that any other `.env.*` file with production / staging environment credentials
is not committed in the repo.

## PostgreSQL Setup

---

After successful installation of postgresql, run the following commands **one by one** on the command prompt

```bash
sudo service postgresql start # start the postgresql service
sudo -i -u postgres # postgres shell login as postgres user
createuser testuser  # create new user 'testuser'
createdb testdb -O testuser  # create new db using user 'testuser'
psql testdb  # start postgres shell and use database 'testdb'
alter user testuser with password 'test';  # attach password 'test' to user 'testuser'
create schema test;  # create new schema on testdb
grant all privileges on database testdb to testuser;
grant all privileges on schema test to testuser;
```

This will basically setup a user, database and schema as needed per the local development environment.
Once this is done, each time the app server is started, run the following commands to start the postgres
server locally for testing and development purposes. Technically this will setup the `test` profile only.
Use the same steps to setup the `dev` profile. To start the postgres shell run:

```bash
sudo -i -u postgres
psql testdb  # psql devdb for dev profile
```

## Code Formatting and Styling

---

We use the [yapf tool by Google](https://github.com/google/yapf) as our code formatter and styling validation tool.
The styling configuration is contained in [.style.yapf](.style.yapf). It is a modified copy of [Google's Python style guide](https://google.github.io/styleguide/pyguide.html).
Run this command to review the code styling changes that might be required for the code to be compliant with our guidelines.

```bash
yapf -rp --verbose --diff app
```

## Starting Local Server

---

To start the app server in development mode (with auto reload on code changes) locally run

```bash
# make sure that postgres is running already
uvicorn app.main:app --reload
```

or use the script

```bash
# make sure that postgres is running already
bash run.sh
```

# **Boilerplate API with Blacksheep Framework**

OpenApi Documentation can be found at http://127.0.0.1:8080/docs

## 🌐 **API**

### ⚙️ **Setup**

A table containing environment variables for <text style="color: red">local</text> development is provided below. _Variables for database connections, authentication, and other sensitive information must be changed for non-local development._

<details>
<summary>Environment Variables</summary>

| Env Variable | Local Value | Description & Usage |
| --- | --- | --- |
| `DB_HOST` | `"localhost"` | The host for the PostgreSQL database |
| `DB_NAME` | `"postgres"` | The name of the PostgreSQL database |
| `DB_PASS` | `"password"` | The password for the PostgreSQL database |
| `DB_PORT` | `6543` | The port for the PostgreSQL database |
| `DB_USER`  | `"dev"` |The user of the PostgreSQL database (PostgreSQL requires this) |
| `ENVIRONMENT` | `"local"` | Denotes the current development environment |
| `SHOW_ERROR_DETAILS` | `False` | Allows exception details to be surfaced directly from failing web requests as described [here]("https://www.neoteroi.dev/blacksheep/application/#handling-errors"). To avoid security issues, this is `False` by default and will only be `True` when `ENVIRONMENT="local"` |

</details>
<br/>

After cloning this repo and opening the project in your IDE (I am using Visual Studio Code), you should see a project structure similar to this:
```
.
├── Dockerfile
├── Makefile
├── Readme.md
├── api
│   ├── constants.py
│   ├── db
│   │   ├── piccolo_app.py
│   │   ├── piccolo_migrations
│   │   ├── scripts
│   │   │   └── seed.sql
│   │   └── tables
│   │       ├── cat.py
│   │       └── person.py
│   ├── models
│   │   ├── cat.py
│   │   └── person.py
│   ├── server.py
│   └── tools.py
├── compose-dev.yaml
├── docker-compose.yml
├── piccolo_conf.py
└── requirements.txt
```

To get started, from the project root, create your virtual environment:
- For `venv` users, use: `python3 -m venv api && source api/bin/activate`
- Next, set up the database and api in their respective docker containers with: `make setup-containers`
- To start the app itself, run: `make api-start-local` or `uvicorn api.server:app --port 8080 --reload --log-level info`

---

### 🟢 **Startup & Commands**

A table containing the startup and task commands is produced below

<details>
<summary>Startup & Task Commands</summary>

<br/>

| Command | Description |
| --- | --- |
| `make api-start-local` | Starts the api (assuming containers are already running successfully) |
| `make setup-containers` | Sets up `db` and `api` containers |

> 👉 As of 10/04/2023, there may be an issue with the `make api-start-local` command. If the following error is encountered, use `uvicorn api.server:app --port 8080 --reload --log-level info` to start the app instead:
>
> `Opening database connection pool...
/usr/local/lib/python3.12/asyncio/events.py:84: Warning: Unable to fetch server version: Multiple exceptions: [Errno 111] Connect call failed ('127.0.0.1', 6543), [Errno 99] Cannot assign requested address
  self._context.run(self._callback, *self._args)
Unable to connect to the database. Details:
Multiple exceptions: [Errno 111] Connect call failed ('127.0.0.1', 6543), [Errno 99] Cannot assign requested address`

</details>

---

### 🗄️ **Data & Migrations**

Migrations are managed with the `piccolo` package.

New migrations need to be created whenever there is a change to the database schema. To create a new migration, use the following (always include a brief description): `piccolo migrations new db --desc="good description of migration here"`.

To apply the migration, use `piccolo migrations forwards all`.

<!-- #### 😇 **Best Practices**

---

## 🦄 **APP (UI)**

---

### ⚙️ **Setup** -->

---

## 📔 **RESOURCES & REFERENCES**

[1] [Simple CRUD REST API with Blacksheep and Piccolo ORM by Carlos Armando Marcano Vargas](https://medium.com/@carlosmarcano2704/simple-crud-rest-api-with-blacksheep-and-piccolo-orm-698e6e85ae80)

[2] [Auto Migrations (from the Piccolo blog)](https://piccolo-orm.com/blog/auto-migrations/)

[3] [Piccolo ORM](https://piccolo-orm.readthedocs.io/_/downloads/en/latest/pdf/)

---

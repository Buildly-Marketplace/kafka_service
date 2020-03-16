# Kakfa Service

## Development

Build the image:

```bash
docker-compose build
```

Run the web server:

```bash
docker-compose up
```

The API is accessible via the URL `http://localhost:8081`.
User for testing: (username: `admin`, password: `admin`).

Run the tests only once:

```bash
docker-compose run --rm --entrypoint 'bash scripts/run-tests.sh' kakfaservice
```

Run the tests:

```bash
docker-compose run --rm --entrypoint 'bash scripts/run-tests.sh' kakfaservice
```

To run bash:

```bash
docker-compose run --rm --entrypoint 'bash' kakfaservice
```

## Deployment

### Configuration

The following table lists the configurable parameters of buildly and their default values.

|             Parameter               |            Description             |                    Default                |
|-------------------------------------|------------------------------------|-------------------------------------------|
| `ALLOWED_HOSTS`                     | A list of strings representing the domain names the app can serve  | `[]`      |
| `CORS_ORIGIN_WHITELIST`             | A list of origins that are authorized to make cross-site HTTP requests  | `[]` |
| `DATABASE_ENGINE`                   | The database backend to use. (`postgresql`, `mysql`, `sqlite3` or `oracle`) | `` |
| `DATABASE_NAME`                     | The name of the database to use          | ``                                  |
| `DATABASE_USER`                     | The username to use when connecting to the database | ``                       |
| `DATABASE_PASSWORD`                 | The password to use when connecting to the database | ``                       |
| `DATABASE_HOST`                     | The host to use when connecting to the database | ``                           |
| `DATABASE_PORT`                     | The port to use when connecting to the database | ``                           |
| `JWT_PUBLIC_KEY_RSA_BUILDLY`        | The public RSA KEY                       | ``                                  |
| `SECRET_KEY`                        | Used to provide cryptographic signing, and should be set to a unique, unpredictable value | None |
| `KAFKA_TOPIC`                       | The topic that will be subscribed        | None                                |
| `KAFKA_HOSTS`                       | The list of bootstrap servers            | None                                |

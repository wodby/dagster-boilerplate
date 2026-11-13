# Dagster boilerplate

Keep your Dagster assets, jobs and schedules in Git and deploy them with Wodby
as a Dagster code location.

Use it with the [Dagster code location](https://github.com/wodby/service-dagster-code)
service (`dagster-code`) in the
[Dagster stack](https://github.com/wodby/stack-dagster).

## Code

`app/definitions.py` defines the code location's `Definitions`. Add your
assets, jobs, schedules and sensors there, or in other modules of the `app`
package. The code server loads the `app.definitions` module unless the
service's "Python module" setting names another one.

## Python packages

List the packages your code needs in `requirements.txt`. Dagster comes with the
image, at the version of the Dagster webserver and daemon, so don't list
`dagster` itself; Dagster libraries such as `dagster-dbt` must match its
version. The build fails if `requirements.txt` changes Dagster's version.

## Deployments

Every deployment builds a new image and restarts the code server, and Dagster
reloads the code location. Runs are executed inside the code server.

## Files

| Path | Purpose |
| --- | --- |
| `app/` | Your Dagster code |
| `requirements.txt` | Python packages your code needs |
| `.wodby/pipeline.yml` | The Wodby CI pipeline that builds and deploys the image |
| `.dockerignore` | Files left out of the build |

# Meltano Extractor for dummyjson.com (tap-ex1)

`tap-ex1` is a Singer tap for dummyjson.com (It is a exercise :)

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

<!--

Developer TODO: Update the below as needed to correctly describe the install procedure. For instance, if you do not have a PyPi repo, or if you want users to directly install from your git repo, you can modify this step as appropriate.

## Installation

Install from PyPi:

```bash
pipx install tap-ex1
pip install tap-ex1
```

Install from GitHub:

```bash
pipx install git+https://github.com/sajML/meltano-tap-ex1
```

-->

## Usage

You can easily run `tap-ex1` by itself or in a pipeline using [Meltano](https://meltano.com/).




### Create and Run Tests

You can encapsulate the entire workflow in two Docker images: one for Meltano and another for FastAPI. The process can be executed and accessed via http://localhost:8001 with the following command:

```bash
wget https://raw.githubusercontent.com/sajML/meltano-tap-ex1/main/docker-comp-Hub.yaml
docker compose -f docker-comp-Hub.yaml up
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

<!--
Developer TODO:
Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any "TODO" items listed in
the file.
-->

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-ex1
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-ex1 --version
# OR run a test `elt` pipeline:
meltano elt tap-ex1 target-jsonl
```


```bash
docker build -t ex1-tap-img -f Dockerfile.meltano .
docker run --volume $(pwd)/output:/app/output ex1-tap-img
docker run --volume $(pwd)/output:/app/output ex1-tap-img run tap-ex1 target-csv


docker build -t ex1-fastapi-img -f Dockerfile.fastapi .
docker run -p 8001:8000 ex1-fastapi-img
docker run -p 8001:8000 ex1-fastapi-img uvicorn run_api:app --host 0.0.0.0 --port 8000


docker run astro_067921/airflow:latest ls

docker run --volume $(pwd)/output:/app/output sajjadgoudarzi/vicev-ex1-meltano:latest
```
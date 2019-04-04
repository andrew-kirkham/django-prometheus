# Demo Django Prometheus
This repo is a brief demo on how to wire up the beginner Django app with prometheus

## Running
1. Make sure you have Python 3 installed (this was built with Python 3.7)
2. Install requirements with `pip install requirements.txt`
3. Download Prometheus from <https://prometheus.io/download> and run it using the prometheus.yml file in the root of this repo.
    `prometheus --config.file=<this_repo>/prometheus.yml`
    This will start prometheus on the default port 9090
4. Run Django like `python manage.py runserver` which will start on the default port 8000
    metrics are exported on /metrics and you can view them at http://localhost:8000/metrics
    You will need to run migrations with `python manage.py migrate` if you wish to use the admin funcationality at `http://localhost:8000/admin`. To create a superuser you can use `python manage.py createsuperuser`
5. Prometheus should be collecting the metrics and be seen at http://localhost:9090/graph


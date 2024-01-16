# Installation and setup

Install Python interpreter to your computer or use a Docker container to run one. 

```shell
# Install required libraries
python -m pip install -r requirements.txt

# Run application
streamlit run Etusivu.py
```

Deployment is possible in [Streamlit Cloud(https://blog.streamlit.io/host-your-streamlit-app-for-free/)], or on-premise e.g. in a container.

`Dockerfile` contains the runtime environment and it can be utilized like this:

```shell
# build container
docker build -t courses/tikapek24 .

# run container, map local dir to container for quicker dev-time code change reloads
docker run --name tikape-kevat-2024 -it -v `pwd`:/app courses/tikapek24 sh -c "streamlit run Etusivu.py"
```

Connect to http://localhost:8051

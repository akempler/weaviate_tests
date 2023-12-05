# Weaviate Tests and Examples

A docker-compose environment for running weaviate locally for development purposes and testing.

A few examples of using weaviate vector database. 
Most are from the weaviate site itself, with a few of my own tests.

https://weaviate.io/

NOTE: the docker-compose.yml is setup for how I wanted to test on my local environment.
You should configure a docker-compose.yml file for your needs here:  

https://weaviate.io/developers/weaviate/installation/docker-compose

Set an environment variable with your openai key;
export OPENAI_APIKEY=""

Install the requirements if you want to use the python sample files: 

`pip install -r requirements.txt`

Access the ui at: http://localhost:8080/


For local testing, you can run it with ngrok.
```
ngrok http 8080
```
or provide a domain:
```
ngrok http --domain virgil.ngrok.dev 8080
```
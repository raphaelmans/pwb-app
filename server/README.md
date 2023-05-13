### Python Version
`3.11`

### Installation
`pip install virtualenv`
`python3 -m venv env`
`source env/bin/activate`
`pip3 install -r requirements.txt`

### Start Env
`source env/bin/activate`


### Start App
`uvicorn main:app --reload`


### Server
`http://127.0.0.1:8000/`
`http://127.0.0.1:8000/docs`



### Local Database access
`docker exec -it pwbapp-db bash -c "mysql -uroot -p"`
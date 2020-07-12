# trivial

# logic layer

### Requirements
 - Install Python 3
 - Install virtualenv (`pip3 install virtualenv`)
 
 From the `logic_layer` directory:
 - Create a virtual environment
      - run `virtualenv venv -p python3`
 - Activate the venv (`source venv/bin/activate`)
 - Install python dependencies in venv `pip3 install -r requirements.txt`

### Start in Dev mode
 - `python3 dev_app.py`
 
 ### Start in Production mode
 - `gunicorn --bind 0.0.0.0:5000 wsgi:app`
 
 ### Test an endpoint
 - `http://localhost:5000/question/random_question`

# data layer

### Configuration
- MongoDB configs need to be added in `data_layer/mongo_connector/config.py` before starting the service.

### Requirements
 - Install Python 3
 - Install virtualenv (`pip3 install virtualenv`)
 
 From the `data_layer` directory:
 - Create a virtual environment
      - run `virtualenv venv -p python3`
 - Activate the venv (`source venv/bin/activate`)
 - Install python dependencies in venv `pip3 install -r requirements.txt`

### Start in Dev mode
 - `python3 dev_app.py`
 
 ### Start in Production mode
 - `gunicorn --bind 0.0.0.0:5001 wsgi:app`
 
 ### Test an endpoint
 - `http://localhost:5001/question`

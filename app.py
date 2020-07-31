#%%
# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#%%
# Set up database engine
engine = create_engine("sqlite:///hawaii.sqlite")
# Reflect database into classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# Define variables for references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session link
session = Session(engine)

# Define Flask app
app = Flask(__name__)

# Define root
@app.route("/")
# Create Welcome route
def welcome():
    return(
        '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

#%%
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
	filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

#%%
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)



# %%
if __name__ == "__main__":
   app.run(debug=True, port=5001)
# Add all necessary data saves to the app, jsonify and correct for running
import jsonify
import pandas as pd
# will need to run the engine/execute pieces to get this to work

# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

prcp_dict = pd.read_csv('precipitation.csv')
prcp_df = pd.DataFrame(prcp_dict)

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Available routes:" \
           "/api/v1.0/precipitation" \
           "api/v1.0/stations" \
           "/api/v1.0/tobs" \
           "/api/v1.0/<start>" \
           "/api/v1.0/<start>/<end>"
@app.route("/api/v1.0/precipitation")
def prcp():
    print("Server received request for 'Precipitation' page...")
    return

@app.route("/api/v1.0/stations")
def station():
    print("Server received request for 'Station' page...")
    return jsonify(prcp_df)

@app.route("api/v1.0/tobs")
def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.

    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d

    Returns:
        TMIN, TAVE, and TMAX
    """

    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)). \
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

# 4. Define what to do when a user hits the /about route
@app.route("/api/v1.0/<start>")
def about():
    print("Server request to show Start to end of data 'tobs'...")
    return 

if __name__ == "__main__":
    app.run(debug=True)

# Requires BigML Python bindings
#
# Install via: pip install bigml
#
# or clone it:
#   git clone https://github.com/bigmlcom/python.git
from bigml.cluster import Cluster
from bigml.api import BigML
# Downloads and generates a local version of the cluster, if it
# hasn't been downloaded previously.
cluster = Cluster('cluster/609eaaa2e4279b13af006e16',
                  api=BigML("carmenbvg",
                            "f207ec81a0dbbf29f30d583d3001fd19893485bc",
                            domain="bigml.io"))
# To predict centroids fill the desired input_data
# in next line. Numeric fields are compulsory.
input_data = {
    "reservation_status_date.day-of-month": 1,
    "booking_changes": 1,
    "days_in_waiting_list": 1,
    "reservation_status_date.day-of-week": 1,
    "reservation_status_date.year": 1,
    "reservation_status_date.month": 1,
    "babies": 1,
    "children": 1,
    "stays_in_weekend_nights": 1,
    "lead_time": 1,
    "stays_in_week_nights": 1,
    "adults": 1,
    "total_of_special_requests": 1,
    "reservation_status_date": 1,
    "required_car_parking_spaces": 1,
    "adr": 1}
cluster.centroid(input_data)
# The result is a dict with three keys: distance, centroid_name and
# centroid_id
            
 

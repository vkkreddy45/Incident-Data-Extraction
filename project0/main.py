
# -*- coding: utf-8 -*-
# Example main.py
import argparse

import project0

def main(url):
    # Download data
    incident_data = project0.fetchincidents(url)

    # Extract data
    incidents = project0.extractincidents(incident_data)
	
    # Create new database
    db = project0.createdb()
	
    # Insert data
    project0.populatedb(incidents)
	
    # Print incident counts
    project0.status()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)

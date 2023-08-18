#!/usr/bin/env python3

from app import *

def main():

	app.run(
		host="127.0.0.1",  # Run on our localhost, not over the network.
		port=8080,         # Run on port 8080.
		debug=True         # Debug mode auto-updates our app when we save code.
	)

if __name__ == "__main__":
	main()

# Warehouse Inventory Checker
A service to check the inventory of items at Warehouse stores. 

Currently supports the following stores:
* BJs Wholesale Club

## Dependencies:
1. Docker 19.03.10+
1. Docker-compose 1.25.5 (not technically required, but very convenient)

## To build:
1. Run `docker-compose build`

## To use:
1. Create a text file with URLs you which to check the inventory of, with each URL being on a new line.
1. Set the `URL_FILE` variable in a `.env` file or shell variable to the path of the URLs, relative to the 
   docker-compose file. 
1. Set the `INTERVAL` variable to set the number of **minutes** between jobs.
1. Run `docker-compose up -d` to start.

### Development
As a dev convenience, you can use can copy the `docker-compose.dev.yml` file to be a `docker-compose.override.yml` file
to overwrite the entrypoint and bind mount the code into the container for easy editing and execution.

#### Todos: 
* Add e-mail alerts when things are in stock
* Add support for Costco
* Reduce the size of the image (hopefully drastically)
* Investigate why requests take longer than they seemingly should
* Clean up build-time warnings
* Make into proper python package with 
* Proper testing
* CI pipeline
* Allow more customization of job interval as an input to the system
* Find a deployable solution -- cloud service? raspberry pi?


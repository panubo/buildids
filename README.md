# Build IDs

A simple web service to generate incrementing build ids.

## Running

`docker run --rm -t -i -v $(pwd)/data:/data panubo/idgenerator`

## Usage

Request a id for a given sha256 token.

`curl http://<server>/id/<sha256>`

This will return 1, then subsequent requests will increment the value returned.

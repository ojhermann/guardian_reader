# Structure

- [client](#client)
- [functions](#functions)
- [models](#models)
- [static_data](#static_data)
- [services](#services)
- [test](#test)

## `client`

- contains a client for using the [Open Platform](https://open-platform.theguardian.com/)
- also contains models encapsulating the responses

## `functions`

- functions useful in various parts of this service
- sub-package `services`
    - functions used in `services`
    - structure mirrors that of `services`

## `models`

- models used throughout `guardian_reader`
- allowed internal dependencies from `static_data`

## `static_data`

- static data for use in the rest of the repo
- *no dependencies* on `guardian_reader` packages

## `services`

- organized into versions e.g. `v1`
- within a version package, the file name should match (as closely as feasible) the endpoint prefix.

## `test`

- unit testing for `guardian_reader`
- internal structure to match the structure of `guardian_reader`

# Architecture of Flat Easy Finder application

## Status

Accepted.

## Context
At the design stage of the application, functional separation of individual parts of the code should be provided in order to facilitate easier understanding of the code, its modification and further development.

## Decision
Code of application is divided in 3 main functional groups. First one in tracking package and consist all the backend code used for collecting, transforming and data analysis.
Second one is in ui package and is about frontend and communication with a user.


## Consequences

Using data from multiple websites may increase the time needed for web scraping, but it also provides a greater opportunity to draw interesting conclusions.
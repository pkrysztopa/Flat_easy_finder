# Architecture of Flat Easy Finder application

## Status

Accepted.

## Context
At the design stage of the application, functional separation of individual parts of the code should be provided in order to facilitate easier understanding of the code, its modification and further development.

## Decision
Code of application is divided in 3 main functional groups. First one in tracking package and consist all the backend code used for collecting, transforming and data analysis.
Second one is in ui package and is about frontend and communication with a user. In the diagram below you can see the structure of the application.

<img src = "https://github.com/pkrysztopa/Flat_easy_finder/issues/9#issue-1707415177"></img>


## Consequences
Proposed division of the code makes it easier to understand the code and its modification. The application is also easier to develop and test.

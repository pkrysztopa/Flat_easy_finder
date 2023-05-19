# Services used for webscraping

## Status

Accepted.

## Context
The choice of data source is crucial in a data-analytics-driven project. When choosing, technological limitations should be taken into account, as well as for what purpose the data is collected.

## Decision
Ultimately, the goal is to collect data from all major polish real estate websites. Gathering all possible data together can give unique opportunities for an in-depth analysis of the real estate market.
At the beginning, it was decided to focus on one portal, otodom.pl, due to its clear structure and well-ordered display of data. Once the analytical layer of the software and the layer of communication with the user are completed, more portals will be added.

## Consequences

Using data from multiple websites may increase the time needed for web scraping, but it also provides a greater opportunity to draw interesting conclusions.
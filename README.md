# Beyond The FDA: Drug-Related Adverse Events in 2017


<iframe width="560" height="315" src="https://www.youtube.com/embed/4FnveHiDEYk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



## Introduction
We have built an exploratory web application (via Flask & Dash) that allows users to get information about FDA-regulated drugs (and their reactions) that were involved in "Adverse Events" reported to the FDA across different US holidays in 2017. Users are able to choose statistics and visualizations generated from a pre-defined set of SQLAlchemy queries.

The [FDA](https://fis.fda.gov/extensions/fpdwidgets/2e01da82-13fe-40e0-8c38-4da505737e36.html) defines Adverse Events (AE) as "...any symptom that occurs while taking a drug, which may or may not have been caused by the drug. This is different from an adverse drug reaction (ADR), where there is specific evidence that the AE is related to the drug. A side effect is the same as an ADR. As a result, ADR is always an AE, but an AE may or may not be an ADR."

Some questions that our app might help answer include:
- What were the most common drugs involved with adverse events during the holidays in 2017?
- What were the most common reactions reported during Adverse Events?
- On which holidays were the highest number of deaths, suicides, and attempted suicides reported?

## Gathering The Data
To collect the data, we queried the [FDA's API Drug Adverse Events endpoint](https://open.fda.gov/apis/drug/event/). This data was quite messy – in it were duplicate values in different fields, different structures for the same data, and clearly-impossible values for certain fields (e.g. 1000+ numbers for some ages). Cleaning the data and getting it into a workable format took the vast majority of our time. We attribute the state of the data to the fact that any medical professional can report AEs to the FDA, which introduces human error.

![alt text](https://github.com/anthonytapias/Adverse-Drug-Events-A-Deep-Dive-Into-The-FDA/blob/master/img/Screen%20Shot%202019-01-14%20at%207.45.40%20PM.png)

## Building The Database
After we got our data into a workable state, we then used [SQLAlchemy](https://www.sqlalchemy.org/) to store it in a relational database (you can view the code for that in the [models.py](https://github.com/anthonytapias/Adverse-Drug-Events-A-Deep-Dive-Into-The-FDA/blob/master/dash_package/models.py) file).  Because we wanted to focus on the narrative that users could create across drugs, drug brands, reported reactions, and holidays, we create six tables. Of these six, we had an association table as well as multiple tables modeling one:many and many:many relationships.

## Constructing The Queries
We then created queries (in the queries.py file) for the frontend of our app. Users could use drop-down menus to view the outputs of select queries. These queries included the number of adverse events for a given holiday or the top five reactions for a specific holiday that was choosen on the front end. 

## Creating The Visualizations
For visualizations, we created several pie charts and graphs. These were written in HTML and displayed via Flask and Dash. One interesting find generated from our visual analyses was that auto-immune disease medications came up frequently across all holidays as being involved in adverse events. 
![alt text](https://github.com/anthonytapias/Adverse-Drug-Events-A-Deep-Dive-Into-The-FDA/blob/master/img/top_five_reactions_christmas.png)
![alt text](https://github.com/anthonytapias/Adverse-Drug-Events-A-Deep-Dive-Into-The-FDA/blob/master/img/top_5_brands_reactions_all_holidays.png)

## Deployment
After creating our visualizations we set up to run our server through the run.py file in order to deply the Flask app.

## Future Plans
In the future, we hope to build a website to host our app, so that users don't have to run the code themselves in order to interact with it.

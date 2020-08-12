## Weekly updates for stand-up


### Week 1
Presenter: Maureen

### Week 2
Presenter: Cindy

### Week 3
Presenter: Isaac

### Week 4:
Presenter: Feli

### Week 5
Presenter: Maureen

Completed tasks for this week:

1. Expanded from last week's model to look at pedestrian & cyclist collisions that resulted in injuries and extracted important features.

- Note that collisions involving pedestrians and cyclists account for ~7% of the reports in the cleaned dataset. 
- 31% of all collisions resulted in at least 1 injury (injury/serious injury/fatality).
- 90% of collisions involving pedestrians or cyclists resulted in an injury.
- 27% of collisions NOT involving pedestrians or cyclists resulted in an injury.

![feature0]
![feature1](figures/lightgbm_importance_allcoll.png)
![feature2](figures/lightgbm_importance_ped_cyclist.png)
![feature3](figures/lightgbm_importance_caronly.png)



2. Combined Intersections and Traffic Flow data with Collisions data. 





Also implemented different models to see how they compared (LightGBM, Catboost, RandomForest)
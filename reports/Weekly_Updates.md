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

![feature0](figures/combined_importances_lgb.png)
![feature1](figures/lightgbm_importance_allcoll.png)
![feature2](figures/lightgbm_importance_ped_cyclist.png)
![feature3](figures/lightgbm_importance_caronly.png)



2. Combined Intersections and Traffic Flow data with Collisions data. 

3. Developed aggregate data model, predicting annual collisions, to look at intersections rather than streets

- Usable features are harder to come by but seeing the importance of traffic signal type (especially for pedestrian/cyclist collisions) is telling

<img src="https://raw.githubusercontent.com/DataCircles/traffic_collisions_ml_team1/master/reports/figures/Intersections_onlypedcycles_features.png" width="500">
<img src="https://raw.githubusercontent.com/DataCircles/traffic_collisions_ml_team1/master/reports/figures/Collisionrate_differentsignals_onlypedcycles.png" width="435">
<br><br>
<img src="https://raw.githubusercontent.com/DataCircles/traffic_collisions_ml_team1/master/reports/figures/Intersections_allcollisions_features.png" width="500">
<img src="https://raw.githubusercontent.com/DataCircles/traffic_collisions_ml_team1/master/reports/figures/Collisionrate_differentsignals.png" width="435">
<br>

### Miscellaneous Analysis discoveries on merged WSDOT dataset

- <b>1.</b> 65+ year-old drivers have not contributed to the overall decrease in traffic collisions. 

16-25 year-old drivers and 25-65 year-old drivers show a roughly equal proportionate decrease in collisions. 
True number of drivers in each bracket would be needed for a better understanding.


<img src="https://raw.githubusercontent.com/DataCircles/traffic_collisions_ml_team1/master/reports/figures/Collisions_agegroup.png" width="600"><br>
Tableau chart: https://public.tableau.com/profile/isaac.campbell.smith#!/vizhome/SeattleTrafficCollisions_15971158097880/AgeGroups

- <b>2.</b> Annual drunk driving collisions have been remarkably consistent since 2005. 
Considering all the resources that go into preventing and advertising against drunk driving, it may be worth finding newer creative options or harsher p enalties. 

<img src="https://raw.githubusercontent.com/DataCircles/traffic_collisions_ml_team1/master/reports/figures/Collisions_drunk.png" width="600"><br>
Tableau chart: https://public.tableau.com/profile/isaac.campbell.smith#!/vizhome/SeattleTrafficCollisions_15971158097880/DrunkDriving

- <b>3.</b> Data suggests a decrease in collisions from 2012-2015 if it weren't for a dramatic increase in 'distracted driving'

<img src="https://raw.githubusercontent.com/DataCircles/traffic_collisions_ml_team1/master/reports/figures/Distracted_Collisions.png" width="600"><br>
Tableau chart: https://public.tableau.com/profile/isaac.campbell.smith#!/vizhome/SeattleTrafficCollisions_15971158097880/Distracted

Also implemented different models to see how they compared (LightGBM, Catboost, RandomForest)
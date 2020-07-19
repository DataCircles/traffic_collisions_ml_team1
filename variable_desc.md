# COLLISIONS: ALL COLUMNS

**X** - longitude, the GPS values moving left to right (East and West) along the X axis  
**Y** - latitude, represented by horizontal lines, which go up and down (North and South)  
**OBJECTID** - ESRI unique identifier  
**INCKEY** - a unique key for the incident, variable type: Long  
**COLDETKEY** - a secondary key for the incident, variable type: Long  
**REPORTNO** - unknown  
**STATUS** - unknown  
**ADDRTYPE** - Collision address location type, variable type: text, 12 VARCHAR, e.g. Alley, Block, Intersection  
**INTKEY** - a key that corresponds to the intersection associated with a collision, variable type: Double  
**LOCATION** - a text description of location, e.g. TERRY AVE BETWEEN JAMES ST AND CHERRY ST  
**EXCEPTRSNCODE** - unknown  
**EXCEPTRSNDESC** - unknown  
**SEVERITYCODE** - a code that corresponds to the severity of the collision:  
$\,\,$ 3 — fatality  
$\,\,$ 2b — serious injury  
$\,\,$ 2 — injury  
$\,\,$ 1 — prop damage  
$\,\,$ 0 — unknown  
**SEVERITYDESC** - a description of the collision, e.g. Property Damage Only Collision, Injury Collision  
**COLLISIONTYPE** - a description of the collision type, e.g. Parked Car, Rear Ended, Sideswipe  
**PERSONCOUNT** - the total number of people involved  
**PEDCOUNT** - the total number of pedestrians involved  
**PEDCYLCOUNT** - the total number of cyclists involved  
**VEHCOUNT** - the total number of vehicles involved  
**INJURIES** - the total number of injuries other than fatal or disabling at the scene, including broken fingers or toes, abrasions, etc.  
**SERIOUSINJURIES** - total number of injuries that result in at least a temporary impairment, e.g. a broken limb. It does not mean that the collision resulted in a permanent disability  
**FATALITIES** - includes the total number of persons who died at the scene of the collisions, were dead on arrival at the hospital, or died within 30 days of the collision from collision-related injuries  
**INCDATE** - incident date  
**INCDTTM** - date and time of the incident, variable type: text, 30 VARCHAR  
**JUNCTIONTYPE** - category of the junction where the collision took place  
**SDOT_COLCODE** - the SDOT collision code  
**SDOT_COLDESC** - a description of the collision corresponding to the collision code  
**INATTENTIONIND** - whether or not collision was due to inattention. (Y/N)  
**UNDERINFL** - whether or not the driver was under the influence of alcohol or drugs  
**WEATHER** - a description of the weather, e.g. Raining, Clear  
**ROADCOND** - a description of the road conditions, e.g. Dry, Wet  
**LIGHTCOND** - a description of the light conditions, e.g. Dark - No Street Lights, Daylight  
**PEDROWNOTGRNT** - whether or not the pedestrian right of way was not granted. (Y/N)  
**SDOTCOLNUM** - unknown  
**SPEEDING** - whether or not the driver was speeding  
**ST_COLCODE** - code provided by the state that describes the collision, for example: $\,\,$ 0 - Vehicle Going Straight Hits Pedestrian  
$\,\,$ 1 - Vehicle Turning Right Hits Pedestrian  
$\,\,$ 2 - Vehicle Turning Left Hits Pedestrian  
$\,\,$ 3 - Vehicle Backing Hits Pedestrian  
$\,\,$ 4 - Vehicle Hits Pedestrian - All Other Actions  
$\,\,$ 5 - Vehicle Hits Pedestrian - Actions Not Stated  
$\,\,$ 10 - Entering At Angle  
$\,\,$ 11 - From Same Direction - Both Going Straight - Both Moving - Sideswipe  
$\,\,$ 12 - From Same Direction - Both Going Straight - One Stopped - Sideswipe  
$\,\,$ 13 - From Same Direction - Both Going Straight - Both Moving - Rear End  
$\,\,$ ...  
**ST_COLDESC** - a description that corresponds to the state’s coding designation  
**SEGLANEKEY** - a key for the lane segment in which the collision occurred  
**CROSSWALKKEY** - a key for the crosswalk at which the collision occurred  


## COLLISIONS: more relevant columns (according to EDA workshop)  
##### Numeric
- PERSONCOUNT (# of people invovled)  
- PEDCOUNT (# of pedestirans)  
- PEDCYLCOUNT (# of cyclists)  
- VEHCOUNT (# of vehicles)
- INJURIES (# of injuries)
- SERIOUSINJURIES (# of serious injuries)
- FATALITIES (# of deaths)  

##### Human factors
- INATTENTIONIND (whether or not collision was due to inattention)
- UNDERINFL (whether or not a driver involved was under the influence)
- PEDROWNOTGRNT(Whether pedestrian had the right of way)
- SPEEDING (whether or not speeding was a factor in the collision)
- ST_COLCODE (collision type label)


##### Characteristics of the site
- ADDRTYPE (address type)
- LOCATION (described in street names)
- X & Y (GPS location)
- CROSSWALKKEY (crosswalk label)
- JUNCTIONTYPE (junction type)
- ROADCOND (road condition)

##### External factors
- LIGHTCOND (light condition)
- WEATHER (description of the weather conditions during the time of the collision)


# Seattle Streets Data

**Columns**:

- Arterial Classification
- Street Names
- Block Number
- Direction
- One-way
- Surface Width
- Surface Type
- Pavement Condition
- Speed Limit
- Percent Slope
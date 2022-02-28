from imports import *
import acquire as acq

def prep_iris(db):
	iris=acq.get_iris_data()
	iris2=iris.drop(['species_id','measurement_id'],axis=1)
	iris3=iris2.rename({'species_name':'species'},axis=1)
	dummy_df = pd.get_dummies(iris3.species, dummy_na=False, drop_first=True)
	iris4 = pd.concat([iris3, dummy_df], axis=1)
	return iris4
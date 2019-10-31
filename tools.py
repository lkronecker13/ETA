import pandas as pd
import numpy as np

def split_trips(df_per_trip):
    
    df_per_trip = df_per_trip.reset_index(drop=False)
    
    first_stop_set = set(df_per_trip.loc[df_per_trip['stop_offset'] == min(df_per_trip['stop_offset'].values)]['rt_stop_id'].values)

    # Sanity check to see there are no several different departure stops in the same route 
    # (which would not make sense)
    assert len(first_stop_set)==1, 'More than one first stop found for trip: ' + str(set(df_per_trip['rt_trip_id'].values)) + ' Found: ' + str(df_per_trip.loc[df_per_trip['stop_offset'] == 0]['rt_stop_id'].values) 

    # Get indexes of the first stop in each route
    first_stop_route = df_per_trip.loc[df_per_trip['stop_offset'] == min(df_per_trip['stop_offset'].values)]['rt_stop_id'].values[0]
    first_stop_indexes = df_per_trip.index[df_per_trip['rt_stop_id'] == first_stop_route].tolist()
    
    # If there is only one initial stop that means that we only have data for one trip. Return that
    if(len(first_stop_indexes)) == 1:
        return [df_per_trip]

    count = 0
    df_list_trips = []
    for i in range(len(first_stop_indexes)):
        from_index = first_stop_indexes[i]

        if i + 1 == len(first_stop_indexes):
            to_index = df_per_trip.shape[0]
        else:
            to_index = first_stop_indexes[i+1]

        df_trip = df_per_trip[from_index:to_index]

        df_list_trips.append(df_trip)
        count = 1
    
    ### SANITY CHECK
    # Let's make sure that the number of split trips is equal to the number of first stops. 
    assert len(df_list_trips) == len(first_stop_indexes)
        
    return df_list_trips
    
    
def compute_scores(dataframe, predicted, optimal_time, conf_arrival_int):
    scores = [0]
    for index, row in dataframe.iterrows():
        if index == 0:
            continue
        
        scoring_list = list(range(conf_arrival_int))
        score = 0
        row_optimal_time = pd.to_datetime(row[optimal_time])
        conf_arrival_interval = pd.Timedelta(seconds = conf_arrival_int)
        
        earliest_user_arr = row_optimal_time - pd.Timedelta(seconds = conf_arrival_int*60)
        if row_optimal_time - conf_arrival_interval  <= pd.to_datetime(row[predicted]) <= row_optimal_time + conf_arrival_interval:
            score = 1
        else:
            # Assign corresponding score over the interval of time of conf_arrival_interval minutes divided by the index of the 
            # index of the bin
            for i in scoring_list:
                lower_bound = row_optimal_time - pd.Timedelta(seconds=i*60)
                upper_bound = lower_bound - pd.Timedelta(seconds=60)
                
                if upper_bound < pd.to_datetime(row[predicted]) < lower_bound:
                    score = 1/(scoring_list[i]+1)
        scores.append(score)           
    return scores        
       
def score_eta_predictions(dataframe, predicted, optimal_time, conf_arrival_interval):
    scores = compute_scores(dataframe, predicted, optimal_time, conf_arrival_interval)
    return np.mean(scores), scores


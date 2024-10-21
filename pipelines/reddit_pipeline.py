from etls.reddit_etls import connect_to_reddit
from utils.constants import CLIENT_ID, SECRET


def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):

    ############## 1. Connecting to reddit instance ###################################
    instance  = connect_to_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')


    ############## 2. Extraction ######################################################
    posts = extract_posts(instance, subreddit, time_filter, limit)


    ############## 3. Transformation  #################################################

    ############## 4. Loading ti CSV  #################################################
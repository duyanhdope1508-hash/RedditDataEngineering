import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

SECRET = parser.get('api_keys', 'reddit_secret_key')
CLIENT_ID = parser.get('api_keys', 'reddit_client_id')

REDDIT_SUBREDDIT = parser.get('reddit', 'subreddit', fallback='dataengineering')
REDDIT_TIME_FILTER = parser.get('reddit', 'time_filter', fallback='day')
REDDIT_POST_LIMIT = parser.getint('reddit', 'post_limit', fallback=100)
REDDIT_USER_AGENT = parser.get('reddit', 'user_agent', fallback='PersonalRedditAnalytics/1.0')

DATABASE_HOST =  parser.get('database', 'database_host')
DATABASE_NAME =  parser.get('database', 'database_name')
DATABASE_PORT =  parser.get('database', 'database_port')
DATABASE_USER =  parser.get('database', 'database_username')
DATABASE_PASSWORD =  parser.get('database', 'database_password')

#AWS
AWS_ACCESS_KEY_ID = parser.get('aws', 'aws_access_key_id')
AWS_ACCESS_KEY = parser.get('aws', 'aws_secret_access_key')
AWS_REGION = parser.get('aws', 'aws_region')
AWS_BUCKET_NAME = parser.get('aws', 'aws_bucket_name')

INPUT_PATH = parser.get('file_paths', 'input_path')
OUTPUT_PATH = parser.get('file_paths', 'output_path')

POST_FIELDS = (
    'id',
    'title',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'upvote_ratio',
    'subreddit',
    'permalink',
    'over_18',
    'edited',
    'spoiler',
    'stickied'
)

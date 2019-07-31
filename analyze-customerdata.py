import json
from google.cloud import bigquery
from os import environ
from google.oauth2 import service_account


if environ.get('GOOGLE_APPLICATION_CREDENTIALS_STR' ) is None:
    print("Missing Credentials for accessing Google services. ...Exiting")
    exit(1)


info = json.loads(environ.get('GOOGLE_APPLICATION_CREDENTIALS_STR'))
credentials = service_account.Credentials.from_service_account_info(info)
client = bigquery.Client(project='festive-sunbeam-186117', credentials=credentials)

# Perform a query.
QUERY = 'SELECT state,count(*) val  FROM `festive-sunbeam-186117.Customer360.customer` group by state order by 1 desc'
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish

for row in rows:
    print(row.state, row.val)

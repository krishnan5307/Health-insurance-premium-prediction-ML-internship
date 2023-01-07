from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory
from insurance.exception import InsuranceException
import logging,sys

       
cloud_config= {
         ##'secure_connect_bundle': '<</PATH/TO/>>secure-connect-health-insurance-premium-prediction.zip'
         'secure_connect_bundle': 'secure_bundle\secure-connect-health-insurance-premium-prediction.zip'
         
}

auth_provider = PlainTextAuthProvider('lXSEkrnNwjRAZIMrrqDofZEt', 'Ky3RyksHe+NXdWbSsz7zAfkR5wZgodh-I4ZCmL,1Z.SvT7freEDqrB-Ffr2L5SddiRzX7NqYMXo28.PH7lrQ839wn1wz3DqBC-QUMi1550_4ZramWzGz5GMsgAthZC5E')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

class connect_database:

      
      def __init__(self):            
            try:
                  self.cloud_config= cloud_config
                  self.auth_provider= auth_provider
                  self.cluster = cluster
                  self.session = session

            except Exception as e:
                  raise InsuranceException(e,sys) from e      

      def get_db_connection(self) -> session:
            try:
                  self.session.row_factory = dict_factory
                  row = session.execute("select release_version from system.local").one()
                  if row:
                        logging.info(f"Successfully connected to cassandra database: 'health-insurance-premium-prediction' :[{row[0]}]")  
                  return self.session
            
            except Exception as e:
                  logging.info(f"error occured while connecting to database")
                  raise InsuranceException(e,sys) from e         

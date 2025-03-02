import logging
from dotenv import load_dotenv
import os
import pytest
from cc_clients_python_lib.flink_client import FLINK_CONFIG
from ccaf_housekeeping_python_lib.drop_table_with_associated_resources import DropTableWithAssociatedResources


__copyright__  = "Copyright (c) 2025 Jeffrey Jonathan Jennings"
__credits__    = ["Jeffrey Jonathan Jennings (J3)"]
__maintainer__ = "Jeffrey Jonathan Jennings (J3)"
__email__      = "j3@thej3.com"
__status__     = "dev"
 

# Configure the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# Initialize the global variables.
config = {}
statement_name = ""
catalog_name = ""
database_name = ""


@pytest.fixture(autouse=True)
def load_configurations():
    """Load the Schema Registry Cluster configuration and Kafka test topic from the environment variables."""
    load_dotenv()
 
    # Set the Flink configuration.
    global config
    config[FLINK_CONFIG["flink_api_key"]] = os.getenv("FLINK_API_KEY")
    config[FLINK_CONFIG["flink_api_secret"]] = os.getenv("FLINK_API_SECRET")
    config[FLINK_CONFIG["organization_id"]] = os.getenv("ORGANIZATION_ID")
    config[FLINK_CONFIG["environment_id"]] = os.getenv("ENVIRONMENT_ID")
    config[FLINK_CONFIG["cloud_provider"]] = os.getenv("CLOUD_PROVIDER")
    config[FLINK_CONFIG["cloud_region"]] = os.getenv("CLOUD_REGION")
    config[FLINK_CONFIG["compute_pool_id"]] = os.getenv("COMPUTE_POOL_ID")
    config[FLINK_CONFIG["principal_id"]] = os.getenv("PRINCIPAL_ID")
    config[FLINK_CONFIG["confluent_cloud_api_key"]] = os.getenv("CONFLUENT_CLOUD_API_KEY")
    config[FLINK_CONFIG["confluent_cloud_api_secret"]] = os.getenv("CONFLUENT_CLOUD_API_SECRET")
    

    # Set the Flink SQL catalog and database names.
    global catalog_name
    global database_name
    catalog_name = os.getenv("FLINK_CATALOG_NAME")
    database_name = os.getenv("FLINK_DATABASE_NAME")


def test_drop_table():
    """Test the drop_table method."""
    # Instantiate the DropTableWithAssociatedResources class.
    drop_table_class = DropTableWithAssociatedResources(config)

    # Drop the table.
    table_name = "hello"
    result, error_message = drop_table_class.drop_table(catalog_name, database_name, table_name)
    assert result


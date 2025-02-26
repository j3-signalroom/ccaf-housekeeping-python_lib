from cc_clients_python_lib.flink_sql_client import FlinkSqlClient
from cc_clients_python_lib.common import HttpStatus


__copyright__  = "Copyright (c) 2025 Jeffrey Jonathan Jennings"
__license__    = "MIT"
__credits__    = ["Jeffrey Jonathan Jennings (J3)"]
__maintainer__ = "Jeffrey Jonathan Jennings (J3)"
__email__      = "j3@thej3.com"
__status__     = "dev"


class DropTableWithAssociatedResources():
    def __init__(self, flink_sql_config: dict):
        # Instantiate the FlinkSqlClient classs.
        self.flink_client = FlinkSqlClient(flink_sql_config)

    def drop_table(self, catalog_name: str, database_name: str, table_name: str):
        http_status_code, error_message, response = flink_client.submit_statement("drop-statement",
                                                                              "DROP TABLE IF EXISTS hello;", 
                                                                              {"sql.current-catalog": catalog_name, "sql.current-database": database_name})

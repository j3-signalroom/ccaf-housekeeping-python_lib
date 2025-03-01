from typing import Tuple
from cc_clients_python_lib.flink_client import FlinkClient
from cc_clients_python_lib.http_status import HttpStatus


__copyright__  = "Copyright (c) 2025 Jeffrey Jonathan Jennings"
__license__    = "MIT"
__credits__    = ["Jeffrey Jonathan Jennings (J3)"]
__maintainer__ = "Jeffrey Jonathan Jennings (J3)"
__email__      = "j3@thej3.com"
__status__     = "dev"


class DropTableWithAssociatedResources():
    def __init__(self, flink_config: dict):
        # Instantiate the Flink client class.
        self.flink_client = FlinkClient(flink_config)

    def drop_table(self, catalog_name: str, database_name: str, table_name: str) -> Tuple[bool, str]:
        """Drop the table and associated resources."""
        # Get the compute pool.
        http_status_code, error_message, response = self.flink_client.get_compute_pool()
        if http_status_code != HttpStatus.OK:
            return False, error_message

        # Get the statement list.
        page_size = response.get("spec").get("max_cfu")
        http_status_code, error_message, response = self.flink_client.get_statement_list(page_size)
        if http_status_code != HttpStatus.OK:
            return False, error_message

        http_status_code, error_message, response = self.flink_client.submit_statement(f"drop-{table_name}",
                                                                                       f"DROP TABLE IF EXISTS {table_name};", 
                                                                                       {"sql.current-catalog": catalog_name, "sql.current-database": database_name})

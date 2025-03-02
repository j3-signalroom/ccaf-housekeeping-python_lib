from typing import Tuple
import re
import logging
from cc_clients_python_lib.flink_client import FlinkClient
from cc_clients_python_lib.http_status import HttpStatus


__copyright__  = "Copyright (c) 2025 Jeffrey Jonathan Jennings"
__license__    = "MIT"
__credits__    = ["Jeffrey Jonathan Jennings (J3)"]
__maintainer__ = "Jeffrey Jonathan Jennings (J3)"
__email__      = "j3@thej3.com"
__status__     = "dev"



# Configure the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class DropTableWithAssociatedResources():
    def __init__(self, flink_config: dict):
        # Instantiate the Flink client class.
        self.flink_client = FlinkClient(flink_config)

    def drop_table(self, catalog_name: str, database_name: str, table_name: str) -> Tuple[bool, str]:
        pattern = r'(?:drop|from|insert)\s+([-.`*\w+\s]+?)\s*(?=\;|\)|\(|values)'
        

        # Get the statement list.
        http_status_code, error_message, response = self.flink_client.get_statement_list()
        if http_status_code != HttpStatus.OK:
            return False, error_message
        
        # Check if the table exists.
        for item in response:
            phase = item.get("status").get("phase")
            statement_id = item.get("name")
            statement = item.get("spec").get("statement").lower()
            #statement = "select * from `need-to-have-one-environment`.`cluster_0`.`hello` limit 10;"
            catalog_name = item.get("spec").get("properties").get("sql.current-catalog")
            database_name = item.get("spec").get("properties").get("sql.current-database")
            if phase == "FAILED":
                http_status_code, error_message = self.flink_client.delete_statement(statement_id)
                if http_status_code != HttpStatus.ACCEPTED:
                    return False, error_message
            else:
                sql_kind = item.get("status").get("traits").get("sql_kind")
                match = re.search(pattern, statement)
                logger.info("%s, %s, %s, %s", 
                            sql_kind,
                            statement, 
                            phase, 
                            statement_id)
                
                if match:
                    word_between = match.group(1)
                    print("Word between:", word_between)
                else:
                    print("No match found")

        return True, ""

        # # # Drop the table.

        # # http_status_code, error_message, response = self.flink_client.submit_statement(f"drop-{table_name}",
        # #                                                                                f"DROP TABLE IF EXISTS {table_name};", 
        #                                                                                {"sql.current-catalog": catalog_name, "sql.current-database": database_name})

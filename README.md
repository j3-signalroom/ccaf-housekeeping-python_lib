# Confluent Cloud for Apache Flink (CCAF) Housekeeping Library for Python
The CCAF Housekeeping Python Library is a CI/CD support tool designed to automate the teardown of a Flink table and its associated Kafka resources—such as topics and schemas—along with any long-running statements linked to it. This robust automation guarantees that each deployment and test cycle is executed with exceptional consistency and reliability, paving the way for a dynamic and resilient application infrastructure.

**Table of Contents**

<!-- toc -->
- [**1.0 Architecture**](#10-architecture)
+ [**2.0 Resources**](#20-resources)
    * [**2.1 Architecture Design Records (ADRs)**](#21-architecture-design-records-adrs)
    * [**22.2 Managing Flink SQL Statements**](#22-managing-flink-sql-statements)
    * [**2.3 Other**](#23-other)
<!-- tocstop -->

## 1.0 Architecture

## 2.0 Resources

### 2.1 Architecture Design Records (ADRs)
* [001 Architectural Design Record (ADR):  CCAF Housekeeping Library](.blog/adr_001.md)

### 2.2 Managing Flink SQL Statements
* [Monitor and Manage Flink SQL Statements in Confluent Cloud for Apache Flink](https://docs.confluent.io/cloud/current/flink/operate-and-deploy/monitor-statements.html#)
* [DROP TABLE Statement in Confluent Cloud for Apache Flink](https://docs.confluent.io/cloud/current/flink/reference/statements/drop-table.html#:~:text=Dropping%20a%20table%20permanently%20deletes,will%20transition%20to%20DEGRADED%20status._)

### 2.3 Other
* [Confluent Cloud Clients Python Library](https://github.com/j3-signalroom/cc-clients-python_lib)


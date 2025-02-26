# Confluent Cloud for Apache Flink (CCAF) Housekeeping Library for Python
The CCAF Housekeeping Python Library is a CI/CD support tool that automates the teardown and buildup of Table API Flink statements along with their associated Kafka resources—such as topics and schemas—and any continuously executing statements. This powerful automation ensures that every deployment and test cycle is carried out with unmatched consistency and reliability, paving the way for a truly dynamic and resilient application infrastructure.

**Table of Contents**

<!-- toc -->
- [**1.0 Architecture**](#10-architecture)
    * [**1.1 Overview**](#11-overview)
        + [**1.1.1 Tracker service**](#111-tracker-service)
        + [**1.1.2 Housekeeping service**](#112-housekeeping-service)
+ [**2.0 Resources**](#20-resources)
    * [**2.1 Architecture Design Records (ADRs)**](#21-architecture-design-records-adrs)
    * [**22.2 Managing Flink SQL Statements**](#22-managing-flink-sql-statements)
    * [**2.3 Other**](#23-other)
<!-- tocstop -->

## 1.0 Architecture

### 1.1 Overview

#### 1.1.1 Tracker service
CRUD operations for tracking Flink SQL statements and their associated Kafka resources.  Kafka is the persistent store for tracking Flink SQL statements and their associated Kafka resources.

#### 1.1.2 Housekeeping service
Automates the teardown and buildup of Flink SQL statements and their associated Kafka resources.

## 2.0 Resources

### 2.1 Architecture Design Records (ADRs)
* [001 Architectural Design Record (ADR):  CCAF Housekeeping Library](.blog/adr_001.md)

### 2.2 Managing Flink SQL Statements
* [Monitor and Manage Flink SQL Statements in Confluent Cloud for Apache Flink](https://docs.confluent.io/cloud/current/flink/operate-and-deploy/monitor-statements.html#)
* [DROP TABLE Statement in Confluent Cloud for Apache Flink](https://docs.confluent.io/cloud/current/flink/reference/statements/drop-table.html#:~:text=Dropping%20a%20table%20permanently%20deletes,will%20transition%20to%20DEGRADED%20status._)

### 2.3 Other
* [Confluent Cloud Clients Python Library](https://github.com/j3-signalroom/cc-clients-lib)


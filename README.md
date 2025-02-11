# Confluent Cloud for Apache Flink (CCAF) Housekeeping App
The CCAF Housekeeping App is a CI/CD support tool that automates the teardown and buildup of Table API Flink statements along with their associated Kafka resources—such as topics and schemas—and any continuously executing statements. This powerful automation ensures that every deployment and test cycle is carried out with unmatched consistency and reliability, paving the way for a truly dynamic and resilient application infrastructure.

**Table of Contents**

<!-- toc -->
- [**1.0 Architecture**](#10-architecture)
    * [**1.1 Overview**](#11-overview)
        + [**1.1.1 Tracker service**](#111-tracker-service)
        + [**1.1.2 Housekeeping service**](#112-housekeeping-service)
+ [**2.0 Resources**](#20-resources)
    * [**2.1 Architecture Design Records (ADRs)**](#21-architecture-design-records-adrs)
    * [**2.2 API Documentation**](#22-api-documentation)
<!-- tocstop -->

## 1.0 Architecture

### 1.1 Overview

#### 1.1.1 Tracker service
CRUD operations for tracking Flink SQL statements and their associated Kafka resources.
    * Kafka is the persistent store for tracking Flink SQL statements and their associated Kafka resources.

#### 1.1.2 Housekeeping service
Automates the teardown and buildup of Flink SQL statements and their associated Kafka resources.

## 2.0 Resources

### 2.1 Architecture Design Records (ADRs)
* [001 Architectural Design Record (ADR):  CCAF Housekeeping App](.blog/adr_001.md)

### 2.2 API Documentation
* [Flink SQL REST API for Confluent Cloud for Apache Flink](https://docs.confluent.io/cloud/current/flink/operate-and-deploy/flink-rest-api.html)
* [Kafka REST APIs for Confluent Cloud](https://docs.confluent.io/cloud/current/kafka-rest/kafka-rest-cc.html)
* [Confluent Cloud Schema Registry REST API Usage](https://docs.confluent.io/cloud/current/sr/sr-rest-apis.html)

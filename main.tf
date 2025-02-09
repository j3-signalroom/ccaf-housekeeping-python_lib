terraform {
    cloud {
      organization = "signalroom"

        workspaces {
            name = "ccaf-flink-app-tracker"
        }
  }

  required_providers {
        aws = {
            source  = "hashicorp/aws"
            version = "~> 5.86.0"
        }
    }
}


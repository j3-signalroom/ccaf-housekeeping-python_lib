terraform {
    cloud {
      organization = "signalroom"

        workspaces {
            name = "ccaf-statements-tracker-app"
        }
  }

  required_providers {
        aws = {
            source  = "hashicorp/aws"
            version = "~> 5.86.0"
        }
    }
}


terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
    region = "eu-west-2"
}

resource "aws_dynamodb_table" "monty_py" {
    name            = "monty_py"
    hash_key        = "hash"
    billing_mode    = "PAY_PER_REQUEST"
    range_key       = "datetime"
    
    attribute {
        name = "hash"
        type = "S"
    }

    attribute {
        name = "datetime"
        type = "S"
    }

    attribute {
        name = "count"
        type = "N"
    }

    attribute {
        name = "ttl"
        type = "N"
    }

    local_secondary_index {
        name            = "idx_value"
        range_key       = "count"
        projection_type = "KEYS_ONLY"
    }
    
    local_secondary_index {
        name            = "idx_ttl"
        range_key       = "ttl"
        projection_type = "KEYS_ONLY"
    }
    
    ttl {
        attribute_name = "ttl" 
        enabled = true
    }
}

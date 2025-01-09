#!/bin/bash
# This script creates a Heroku app for a specific subproject

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <subproject_name> <heroku_app_name>"
    exit 1
fi

project_name=$1
heroku_app_name=$2

# Navigate to the subproject directory
cd "$project_name" || { echo "Directory $project_name not found!"; exit 1; }

# Create the Heroku app with the specified name and set a unique remote
heroku create "$heroku_app_name" --remote "${project_name}-heroku"

# Confirm success
echo "Heroku app '$heroku_app_name' created and remote '${project_name}-heroku' added."

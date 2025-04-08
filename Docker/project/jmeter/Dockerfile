# Use the official Jenkins LTS image as the base image
FROM jenkins/jenkins:lts

# Optionally switch to root to install any additional packages you may need
USER root

# Example: install Git and Maven (remove or modify these as needed)
RUN apt-get update && apt-get install -y git maven

# Switch back to the Jenkins user
USER jenkins

# (Optional) Expose the default Jenkins ports
EXPOSE 8080
EXPOSE 50000
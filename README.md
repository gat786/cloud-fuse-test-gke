# Testing Mounting of Cloud Storage buckets as Volumes to GKE Pods


This Repository creates a helm chart that deploys a pod with a volume mounted to a GCS bucket.
The pod runs a simple python script that writes to the mounted volume.
The script is run as a cron job every minute.
The script writes the current time to a file in the mounted volume.
The file is then uploaded to the GCS bucket.

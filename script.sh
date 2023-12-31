gcloud iam service-accounts create gcs-test-fuse \
  --project=bhdigital-data-dev

gcloud storage buckets add-iam-policy-binding gs://test-storage-mounting \
    --member "serviceAccount:gcs-test-fuse@bhdigital-data-dev.iam.gserviceaccount.com" \
    --role "roles/storage.admin"

gcloud iam service-accounts add-iam-policy-binding gcs-test-fuse@bhdigital-data-dev.iam.gserviceaccount.com \
    --role roles/iam.workloadIdentityUser \
    --member "serviceAccount:bhdigital-data-dev.svc.id.goog[test-bucket-storage/test-storage-chart]"

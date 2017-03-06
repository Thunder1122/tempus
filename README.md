# tempus
Files for completing internship exercise

StorageAnalysis.py contains a function named BucketAnalysis. BucketAnalysis takes a single AWS S3 bucket to analyze and an integer N specifying a ceratin number of files to return.

BucketAnalysis will then return a tuple of the following values: the bucket name, the date and time the bucket was created, the number of files within the bucket, the total size of the files within the bucket, and a list of the first N (newest or oldest) files.

Other keyword arguments include: "size_format", which defaults to bytes, but can also be set to KB, MB, or GB, modifying the units for which total file size will be reported; "sorting", which can be set to either newest or oldest, and determines whether the N files returned are the N newest or N oldest files modified in the bucket.

IMPORTANT NOTE: This script is intended to function on a SINGLE bucket and must be wrapped into a larger script if desired to run on multiple buckets.

Example procedure for running the script:
Open a python command line, and do the following

$ import StorageAnalysis as sa

$ import boto3

$ s3 = boto3.resource('s3')

$ bucket = list(s3.buckets.all())[0]

$ sa.BucketAnalysis(bucket, N, size_format='KB', sorting='newest')

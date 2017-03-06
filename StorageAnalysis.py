from __future__ import division
import boto3

s3 = boto3.resource('s3')

buckets = list(s3.buckets.all())

def BucketAnalysis(bucket, N, size_format='bytes'):
    # Get the bucket name, and formated date/time
    bucket_name = bucket.name
    bucket_creation = bucket.creation_date.ctime()

    # Find how many objects in this bucket, and store all fo them
    bucket_objects = list(bucket.objects.all())
    object_count = len(bucket_objects)

    # Initialize a variable to store the running total of bytes/KB/MB/GB
    # Sum over object sizes, using unit specified in size_format
    object_size_accumulator = 0
    for obj in bucket_objects:
        if size_format == 'KB':
            object_size_accumulator += (obj.size / (2**10))
        elif size_format == 'MB':
            object_size_accumulator += (obj.size / (2**20))
        elif size_format == 'GB':
            object_size_accumulator += (obj.size / (2**30))
        # Note: using raw number of bytes as the default fall-through
        else:
            object_size_accumulator += int(obj.size)

    return bucket_name, bucket_creation, object_count, object_size_accumulator

print BucketAnalysis(buckets[0], 0, size_format = 'bytes')
from __future__ import division
import boto3


def BucketAnalysis(bucket, N, size_format='bytes', sorting='oldest', grouping=''):
    '''
    Performs simple analysis of an AWS S3 buckets, returning basic info
    like name, created, size, etc...size

    --------------------
    Inputs:
        bucket: AWS S3 bucket -- the desired AWS S3 bucket to retrieve information from
        N: int -- the maximum number of files to return
    --------------------
    Optional Keyword Arguments:
        size_format: str -- the unit of size total file size is returned in,
                     capabale of bytes, KB, MB, and GB. Defaults to bytes
        sorting: str -- the order to sort the N returned files by, either
                 newest first, or oldest first
        grouping: str -- the manner by which all objects in the bucket will
                 be grouped, based on object lifecycle settings
    --------------------
    Outputs:
        Name: the inputted buckets name
        Created: the date and time of creation
        Count: the number of files in the bucket
        Size: the total size of all files in the bucket
        Files: a python array of N files, appropriately sorted
    --------------------
    '''
    # Get the bucket name, and formated date/time
    bucket_name = bucket.name
    bucket_creation = bucket.creation_date.ctime()

    # Find how many objects in this bucket, and store all of them
    bucket_objects = list(bucket.objects.all())
    object_count = len(bucket_objects)

    # Initialize a variable to store the running total of bytes/KB/MB/GB
    # Sum over object sizes, using unit specified in size_format
    object_size_accumulator = 0
    for obj in bucket_objects:
        print obj, obj.last_modified
        if size_format == 'KB':
            object_size_accumulator += (obj.size / (2**10))
        elif size_format == 'MB':
            object_size_accumulator += (obj.size / (2**20))
        elif size_format == 'GB':
            object_size_accumulator += (obj.size / (2**30))
        # Note: using raw number of bytes as the default fall-through
        else:
            object_size_accumulator += int(obj.size)

    # Sort the buckets from oldest to newest based on last_modified
    bucket_objects.sort(key=lambda obj: obj.last_modified)

    # Reverse the order depending on sorting keyword
    if (sorting == 'newest'):
        bucket_objects.reverse()

    # Check to make sure slicing won't throw and index error, then do it
    # If an index error would be thrown, N is larger than the number of objects,
    # so as many objects as possible will be returned rather than N objects
    if object_count > N:
        bucket_objects = bucket_objects[:N]


    return bucket_name, bucket_creation, object_count, object_size_accumulator, bucket_objects
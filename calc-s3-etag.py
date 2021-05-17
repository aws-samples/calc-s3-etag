#// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#// SPDX-License-Identifier: MIT-0

import sys
import hashlib

def calculate_s3_etag(file_path, chunk_size):
    md5s = []

    with open(file_path, 'rb') as fp:
        while True:
            data = fp.read(chunk_size)
            if not data:
                break
            md5s.append(hashlib.md5(data))

    if len(md5s) < 1:
        return '"{}"'.format(hashlib.md5().hexdigest())

    if len(md5s) == 1:
        return '"{}"'.format(md5s[0].hexdigest())

    digests = b''.join(m.digest() for m in md5s)
    digests_md5 = hashlib.md5(digests)
    return '"{}-{}"'.format(digests_md5.hexdigest(), len(md5s))
if len(sys.argv) !=3:
    print("Usage: calc-s3-etag.py {file} {multipart-transfer size}")
    print("")
    print("Multipart transfersize may be gotten by referencing the .aws/config file or by using the following example commands to examine a large object uploaded to the SBE")
    print("aws s3api head-object --bucket {bucketname} --key \"[prefix/]{objectname}\" --endpoint-url {url to SBE device including port}")
    print("take the resulting content length and divide it by the number after the dash in the Etag.  Take that result and divide it by 1048576")
    print("the result will be slightly below the multi-part transfer chunk size measured in MB utilized in the transfer")
    sys.exit(0)
mychunksize=int(sys.argv[2]) * 1024 * 1024
print(calculate_s3_etag(sys.argv[1],mychunksize))

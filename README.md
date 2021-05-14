# calc-s3-etag
When a file is uploaded to S3 or Snowball Edge it has an md5 sum calculated and stored as an etag.  For larger files that are uploaded using multi-part uploads, the etag is in the form of [summary hash]-number of parts.  This summary hash does not match the md5sum of the file and thus makes it difficult for users to clearly verify that the source file matches what is in the target location.  

Using the metadata for a multi-part uploaded file, the chunk size can be roughly determined as it will be about the number of bytes of the object (returned by the s3api head-object command) divided by the number of parts with that result being divided by 1024 * 1024.  

This can then be utilized with this script to calculate the summary etag for comparrison with the online object. 

Future enhancements that anyone can contribute to this repo are:
- performance improvements
- use of getopts to allow for expanded functionality
- added code to actually get the source object and perform the compare
- recursive enablement


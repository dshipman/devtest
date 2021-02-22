# Part 6: Cloud computing

This sections tests some general cloud computing knowledge to do with AWS and cloud infra in general.
It is expected that you will need to find the answers to some of these questions via Google.

Please write your answers in this file.

### Question 6.1

Which AWS region is the closest to Melbourne?

### Question 6.2

What is the name of a cheap AWS EC2 instance that offers _at least_ 12 CPU cores and 16GB of RAM?
What are its specs (CPU cores, RAM) and cost per hour?

How much will it cost to run this instance for two weeks?

### Question 6.3

Provide the AWS CLI command to copy all the contents of a S3 bucket to another S3 bucket on the same account.
The source bucket may contain nested files within "folders".

Source bucket: s3://mysource
Destination bucket: s3://mydest

```bash
# Your command here
```

### Question 6.4

Link to a section of library documentation showing how to stop an AWS EC2 instance using a Python client library (can be a howto, API reference, or tutorial).

### Question 6.5

Describe, in 1-3 sentences

- What an AMI is and why it is useful for running EC2 instances
- What IAM is and why it is useful when administering AWS
- Where you would add your SSH public key onto an EC2 instance in order to log in as the "ubuntu" user

### Question 6.6

Create a new SSH key and paste both the public and private key into this file.

### Question 6.7

Write a bash one liner to create a new file called `foo.txt` which contains the text "Hello World!", followed by a newline

```bash
# Your command here
```

### Question 6.8

Write a bash one liner to create a new file which contains the text "Hello World!", followed by a newline, on a remote machine via SSH.

Remote machine hostname is `foo.com` and the user is `bar`. Assume you have all your SSH keys set up correctly on your machine and the target server.

```bash
# Your command here
```

### Question 6.9

Buildkite it a self-hosted CI system. Referring to the documentation via Google, is it possible to run a scheduled build at 2pm every Tuesday? Please link to the URL of the documentation where you found your answer.

### Question 6.10

GitHub Actions is a CI system provided by GitHub, Referring to the documentation via Google, what is an environment variable that you could use to determine whether your bash script is running inside a Github Action?

What kind of value would indicate that your script is running inside a GitHub Action?

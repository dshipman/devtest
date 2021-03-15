# Part 6: Cloud computing

This sections tests some general cloud computing knowledge to do with AWS and cloud infra in general.
It is expected that you will need to find the answers to some of these questions via Google.

Please write your answers in this file.

### Question 6.1

Which AWS region is the closest to Melbourne?

Asia Pacfic (Sydney) - although it's worth considering that the geographically closest region 
hasn't always been the best (latency-wise) or most cost-effective.  A Melbourne region is 
(meant to be) opening in 2022.

### Question 6.2

What is the name of a cheap AWS EC2 instance that offers _at least_ 12 CPU cores and 16GB of RAM?
What are its specs (CPU cores, RAM) and cost per hour?

Assuming this question refers only to on demand pricing (ie ignore spot instances, reserved etc), and pricing is in Sydney Region (and that CPU cores refers to vCPU rather than physical cores):
a1.4xlarge (16 vCPU, 32GiB memory): $0.5328/hour

How much will it cost to run this instance for two weeks?

$176.00 (0.5328 * 24 * 14)

### Question 6.3

Provide the AWS CLI command to copy all the contents of a S3 bucket to another S3 bucket on the same account.
The source bucket may contain nested files within "folders".

Source bucket: s3://mysource
Destination bucket: s3://mydest

```bash
# Your command here
```
aws s3 cp s3://mysource/ s3://mydest/ --recursive

### Question 6.4

Link to a section of library documentation showing how to stop an AWS EC2 instance using a Python client library (can be a howto, API reference, or tutorial).

https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.stop_instances

### Question 6.5

Describe, in 1-3 sentences

- What an AMI is and why it is useful for running EC2 instances

AMI (Amazon Machine Images) are essentially preconfigured 'virtual machines', including the
VM image themselves, storage configuration, permissions, and device mapping.  Multiple
instances can be started from the same AMI, and AMIs can be run from existing templates
(the modified and saved as a new AMI)


- What IAM is and why it is useful when administering AWS

IAM essentially performs the same role as user access control in operating systems, providing
configuration for users, groups, policies, and what their access rights (permissions) are in
relation to images, storage devices etc.

- Where you would add your SSH public key onto an EC2 instance in order to log in as the "ubuntu" user

/home/ubuntu/.ssh/authorized_keys

### Question 6.6

Create a new SSH key and paste both the public and private key into this file.

Public:

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC7WFtnIEKzEqJq9CgQnuFHLa1LbTrqXMsaa6CzA/NbpUftGx3oIQuo8bNuqJ0931uEkakEo8H4/vulAkR1DnaBcW/zWi9hokiZVg2fZ28R8E87NV1pV0+hnPqATNN+BNHTBC6cASd4HN2YOnZmHXkK9cqtlND1XgGIq7ftKbyYmv4z8wPxpn9JZs5BbLOO5iSw1HoXj2ZhnnmNi8MfbW6v2qCu2eAmKT7dTxYw0S1JrQTzUIP9BC2AuEyNbJfdYHCQYmEgp9dj/c1ZdkSkqVwIqJu637hRxept0bVcyNeYT7SZSVm1aUlaV7Ax+hEV7VAIJlO9QpbDNYEkVoJbq6XP s@DESKTOP-6PENRG3

Private:

-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAu1hbZyBCsxKiavQoEJ7hRy2tS2066lzLGmugswPzW6VH7Rsd
6CELqPGzbqidPd9bhJGpBKPB+P77pQJEdQ52gXFv81ovYaJImVYNn2dvEfBPOzVd
aVdPoZz6gEzTfgTR0wQunAEneBzdmDp2Zh15CvXKrZTQ9V4BiKu37Sm8mJr+M/MD
8aZ/SWbOQWyzjuYksNR6F49mYZ55jYvDH21ur9qgrtngJik+3U8WMNEtSa0E81CD
/QQtgLhMjWyX3WBwkGJhIKfXY/3NWXZEpKlcCKibut+4UcXqbdG1XMjXmE+0mUlZ
tWlJWlewMfoRFe1QCCZTvUKWwzWBJFaCW6ulzwIDAQABAoIBACh1+reZBg66tY03
0fdU+P5wZP7nRlQbWloIaJqA/ewLFC+nLZxWlrgUC1aY3+ze8lr9Qm2YGGp4V0zZ
4oMNbpaiMzVxgs4pSFildye4JQrQxavZ6KS5kJ8s0gUnkn2i+NYEDzTuIuIUCd+4
sJ15PA0b7Hv0qfR0KwyjWYPFAdBLOkvqRDJRXzJJS0RoIbXgRIlwE8JSnFuNhPKm
A62LvsfrN42JwZsqGNONskjwrF4mw+vO2EXQZgOM0jM6BrXFihsddrIkcXPiTgrl
AJPESdBmy/FpAka4OcOVC8NS90E+8uYE30w4k9VZujpA0ss8+fmkSHPQp9CT4gHM
X0JLWWECgYEA6tXyocDAR/Sl9xKFMJjm6t728xtClNG2TsVZ3EG3a1Q5E/V8cvXZ
ddPWW3upmqfBsM9LZ4NiazTaFAnTpve7oW53T39aCLIRQXOE5n94vzLhtGtlG1eu
B5TcMWBtwxwLOwa0J3b+hiGjL74//AfFUeVjQ7AyDDZonNuWkMh05ukCgYEAzDq4
3dJQNp0grBsg2C+DZXyOnHcjfwLeWuPHJdoj5wEENFao76ZjLKpKJAiNqr7NKJ0U
MbJyxc5d9Dezh5l+d6cwc/42jh6OtrS6W32eVaIS7x7Frc1yM+ExJDEMI5Dh+McA
m5j2LKHn1vF7sz2xP9DTA3X75JBHSteFEfl3I/cCgYEAwRoAk+Wttv2DY3FFODri
1wtUwX8O9tSjNo6tX6JiMs1kyfa4yMdEc9EnmL5NLrD3Ym5ysMGmskUZdhTGh6t6
DDqLvUEZRcE20z0scWUsYvxyACu3Tg6BOha8IZYLa76ptXXDuhftH1qVl3K3poS1
Sqx3PXerD8PFrgYa/x72kdECgYBu5Qvw1vxbS2KsUWa6PMJ6XvIJH+AUXXhjnf9L
HHIWQ0UHLm85Af4kCKuNeV+DcWtxPCn0+lK7+dymeYBwhvZW/l+e/FCfRxRzPRtc
Bo/tK75gPTNVtpLmfMb0QfW3cjphnZ1E3//8KEX9Ps7Oexc98aRC4tPOPlGX4AMP
yYfZ7QKBgQCir1z5cirUVA3/r18gKo+/BTrnOuFwqeZec0ilbMqKSkXKmySEEK6F
GKHN/Kxa9EHWzo1HX5p/LSv+VNlmHXxyZTx1RU6NIwdH16Am0PN7A9CZpEqAySwE
gDvLo7b9DgkqOTeRJ4H1lA9yJP/lfw4Bk3NY8Jg4IEdRIz3ebpVZWw==
-----END RSA PRIVATE KEY-----


### Question 6.7

Write a bash one liner to create a new file called `foo.txt` which contains the text "Hello World!", followed by a newline

```bash
# Your command here
```

echo $'Hello World!\n' > foo.txt

### Question 6.8

Write a bash one liner to create a new file which contains the text "Hello World!", followed by a newline, on a remote machine via SSH.

Remote machine hostname is `foo.com` and the user is `bar`. Assume you have all your SSH keys set up correctly on your machine and the target server.

```bash
# Your command here
```
ssh bar@foo.com "echo $'Hello World!\n' > foo.txt"

### Question 6.9

Buildkite it a self-hosted CI system. Referring to the documentation via Google, is it possible to run a scheduled build at 2pm every Tuesday? Please link to the URL of the documentation where you found your answer.

Yes - Buildkite supports any schedule that can be expressed in their (modified) crontab syntax
https://buildkite.com/docs/pipelines/scheduled-builds

### Question 6.10

GitHub Actions is a CI system provided by GitHub, Referring to the documentation via Google, what is an environment variable that you could use to determine whether your bash script is running inside a Github Action?

GITHUB_ACTIONS

What kind of value would indicate that your script is running inside a GitHub Action?

true 
("Always set to true when GitHub Actions is running the workflow." - 
https://docs.github.com/en/actions/reference/environment-variables)
# Nifi-Docker
NiFi docker container customization from the [official Apache Nifi Docker Image](https://hub.docker.com/r/apache/nifi)

### 1. Build Docker
Pull the latest version of Apache Nifi Docker, build and run

```shell
$ docker pull apache/nifi:1.18.0
```
Option 1: Run without authentication
```shell
$ docker run --name nifi -e NIFI_WEB_HTTP_PORT='8080' -p 8080:8080 -d apache/nifi:1.18.0
```
Open the URL http://localhost:8080/nifi.
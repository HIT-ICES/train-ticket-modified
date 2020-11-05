FROM openjdk:8-jre-alpine
MAINTAINER Lei
ADD zipkin-server-2.16.0-exec.jar app.jar
EXPOSE 9411
#ENTRYPOINT ["java","-jar","app.jar", "--STORAGE_TYPE=mysql --MYSQL_USER=root --MYSQL_PASS=123456 --MYSQL_HOST=60.205.188.102 --MYSQL_TCP_PORT=3306"]
ENTRYPOINT ["sh", "-c", "java -jar app.jar --STORAGE_TYPE=mysql --MYSQL_USER=root --MYSQL_PASS=123456 --MYSQL_HOST=60.205.188.102 --MYSQL_TCP_PORT=3306"]
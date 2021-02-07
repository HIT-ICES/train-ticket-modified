FROM openjdk:8-jre-alpine

#RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone

ADD ./target/ts-travels2-service-1.0.jar /app/
CMD ["java", "-Xmx200m", "-jar", "/app/ts-travels2-service-1.0.jar"]

EXPOSE 16346
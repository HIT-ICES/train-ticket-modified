## 复旦火车票系统
原系统[train ticket](https://github.com/FudanSELab/train-ticket)

系统的理解等一些方面，逻辑图：
![](./image/luoji.png)

其余的见[smell定义中](http//60.205.188.102:8080/issue/MCS-87)
### 在原有的系统上进行一些更改



1. 基础镜像的更改：

   将原有的基础镜像**java:8-jre**更改为**openjdk:8-jre-alpine**

   原本的系统只每个服务只部署一个实例（在他的master节点的qui部署下）

2. 数据更改

### 项目运行：
#### zipkin mage to build
~~~shell script
./build-image.sh
~~~
#### compose快速启动

~~~shell script
git clone http://192.168.1.104:12345/BoyLei/train-ricket 
cd train-ticket
mvn clean package -Dmaven.test.skip=true
docker-compose -f docker-compose-change.yml up
~~~

#### kubernetes 快速启动(少镜像)
~~~shell script
git clone http://192.168.1.104:12345/BoyLei/train-ricket cd train-ricket/deploy-k8s-test/
./run.sh
~~~
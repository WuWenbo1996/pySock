# 开发计划
- Stage1: 在master分支完成基本功能：（1）数据接收（2）数据查询服务

    目前存在的问题：使用shell脚本时，无法同时运行两个py文件，会被第一个给堵塞住

- Stage2: 容器化开发，提高部署效率。
- Stage3: 使用`flink`与`kafka`，flink用于数据流处理，kafka作为消息队列。将数据存储和数据接收过程解耦合
参考：(结合资料)[https://blog.csdn.net/feinifi/article/details/121330303]

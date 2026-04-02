# Novena - 个人技术知识库

系统化整理的技术知识库，涵盖中文项目复盘、技术专题沉淀以及英文材料整理。

> 📖 **在线阅读**: [https://kyleexu.github.io/novena](https://kyleexu.github.io/novena)

---

## 中文内容

### 项目经验
#### 行情服务
- [01. 系统结构](zh/project/market/01.%20%E7%B3%BB%E7%BB%9F%E7%BB%93%E6%9E%84.md)
- [02. Flink 任务](zh/project/market/02.%20Flink%20%E4%BB%BB%E5%8A%A1.md)
- [03. 推送技术选型](zh/project/market/03.%20%E6%8E%A8%E9%80%81%E6%8A%80%E6%9C%AF%E9%80%89%E5%9E%8B.md)
- [04. 价格偏差处理](zh/project/market/04.%20%E4%BB%B7%E6%A0%BC%E5%81%8F%E5%B7%AE%E5%A4%84%E7%90%86.md)
- [05. K 线补偿](zh/project/market/05.%20K%20%E7%BA%BF%E8%A1%A5%E5%81%BF.md)
- [06. MQTT 耗时分析](zh/project/market/06.%20MQTT%20%E8%80%97%E6%97%B6%E5%88%86%E6%9E%90.md)
- [07. MQTT 推送结构优化](zh/project/market/07.%20MQTT%20%E6%8E%A8%E9%80%81%E7%BB%93%E6%9E%84%E4%BC%98%E5%8C%96.md)

#### Peanuts 撮合交易系统
- [01. 系统概述](zh/project/peanuts/01.%20%E7%B3%BB%E7%BB%9F%E6%A6%82%E8%BF%B0.md)
- [02. 撮合引擎](zh/project/peanuts/02.%20%E6%92%AE%E5%90%88%E5%BC%95%E6%93%8E.md)
- [03. 订单网关](zh/project/peanuts/03.%20%E8%AE%A2%E5%8D%95%E7%BD%91%E5%85%B3.md)
- [04. 账户服务](zh/project/peanuts/04.%20%E8%B4%A6%E6%88%B7%E6%9C%8D%E5%8A%A1.md)
- [05. 行情服务](zh/project/peanuts/05.%20%E8%A1%8C%E6%83%85%E6%9C%8D%E5%8A%A1.md)
- [06. Aeron 通信层](zh/project/peanuts/06.%20Aeron%20%E9%80%9A%E4%BF%A1%E5%B1%82.md)
- [07. 做市商模块](zh/project/peanuts/07.%20%E5%81%9A%E5%B8%82%E5%95%86%E6%A8%A1%E5%9D%97.md)
- [08. 桥接服务与 Raft](zh/project/peanuts/08.%20%E6%A1%A5%E6%8E%A5%E6%9C%8D%E5%8A%A1%E4%B8%8E%20Raft.md)

#### OTC
- [01. 订单状态](zh/project/otc/01.%20%E8%AE%A2%E5%8D%95%E7%8A%B6%E6%80%81.md)

#### 限流服务
- [01. 概况](zh/project/rate-limit/01.%20%E6%A6%82%E5%86%B5.md)
- [02. 同一毫秒多次请求](zh/project/rate-limit/02.%20%E5%90%8C%E4%B8%80%E6%AF%AB%E7%A7%92%E5%A4%9A%E6%AC%A1%E8%AF%B7%E6%B1%82.md)
- [03. 与单机限流比](zh/project/rate-limit/03.%20%E4%B8%8E%E5%8D%95%E6%9C%BA%E9%99%90%E6%B5%81%E6%AF%94.md)

#### 规则引擎
- [01. 概述](zh/project/rule-engine/01.%20%E6%A6%82%E8%BF%B0.md)

### 香港
#### 税务
- [01. 香港薪俸税指引](zh/hongkong/tax/01.%20%E9%A6%99%E6%B8%AF%E8%96%AA%E4%BF%B8%E7%A8%8E%E6%8C%87%E5%BC%95.md)

### 技术知识库
#### Flink
- [01. flink-architecture](zh/repository/flink/01.%20flink-architecture.md)

#### Java
- [01. 垃圾回收器](zh/repository/java/01.%20%E5%9E%83%E5%9C%BE%E5%9B%9E%E6%94%B6%E5%99%A8.md)

#### Kafka
- [01. 结构](zh/repository/kafka/01.%20%E7%BB%93%E6%9E%84.md)
- [02. 丢失、重复与有序](zh/repository/kafka/02.%20%E4%B8%A2%E5%A4%B1%E3%80%81%E9%87%8D%E5%A4%8D%E4%B8%8E%E6%9C%89%E5%BA%8F.md)

#### MQTT
- [简介](zh/repository/mqtt/%E7%AE%80%E4%BB%8B.md)

#### MySQL
- [01. 并发修改](zh/repository/mysql/01.%20%E5%B9%B6%E5%8F%91%E4%BF%AE%E6%94%B9.md)
- [02. 死锁](zh/repository/mysql/02.%20%E6%AD%BB%E9%94%81.md)
- [03. mvcc](zh/repository/mysql/03.%20mvcc.md)
- [04. for update](zh/repository/mysql/04.%20for%20update.md)

#### 其他
- [01. nonce 与时间戳](zh/repository/others/01.%20nonce%20%E4%B8%8E%E6%97%B6%E9%97%B4%E6%88%B3.md)
- [02. 状态机](zh/repository/others/02.%20%E7%8A%B6%E6%80%81%E6%9C%BA.md)
- [03. 事件驱动](zh/repository/others/03.%20%E4%BA%8B%E4%BB%B6%E9%A9%B1%E5%8A%A8.md)
- [04. 高性能的架构](zh/repository/others/04.%20%E9%AB%98%E6%80%A7%E8%83%BD%E7%9A%84%E6%9E%B6%E6%9E%84.md)
- [05. 零拷贝](zh/repository/others/05.%20%E9%9B%B6%E6%8B%B7%E8%B4%9D.md)
- [06. questions](zh/repository/others/06.%20questions.md)
- [07. 超卖](zh/repository/others/07.%20%E8%B6%85%E5%8D%96.md)

#### Redis
- [01. 数据结构](zh/repository/redis/01.%20%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84.md)
- [02. 分布式锁](zh/repository/redis/02.%20%E5%88%86%E5%B8%83%E5%BC%8F%E9%94%81.md)
- [03. Zset 底层结构](zh/repository/redis/03.%20Zset%20%E5%BA%95%E5%B1%82%E7%BB%93%E6%9E%84.md)

---

## English Content

### Java
- [01. concurrent mark sweep](en/java/01.%20concurrent%20mark%20sweep.md)
- [02. G1](en/java/02.%20G1.md)
- [03. hashmap](en/java/03.%20hashmap.md)
- [04. concurrenthashmap](en/java/04.%20concurrenthashmap.md)
- [05. lock & synchornized](en/java/05.%20lock%20%26%20synchornized.md)

### 行情服务
- [01-system-architecture](en/market/01-system-architecture.md)
- [02-mqtt-vs-websocket](en/market/02-mqtt-vs-websocket.md)
- [03-parallel-vs-serial](en/market/03-parallel-vs-serial.md)
- [04-technical-points](en/market/04-technical-points.md)
- [05-price-deviation-controls](en/market/05-price-deviation-controls.md)
- [05-price-deviation-handling](en/market/05-price-deviation-handling.md)
- [06-latency-analysis](en/market/06-latency-analysis.md)

### 规则引擎
- [01. summary](en/rule-engine/01.%20summary.md)

---

# Novena - 个人技术知识库

系统化整理的技术知识库，涵盖项目经验总结、核心技术栈深度分析以及英文面试准备资料。

> 📖 **在线阅读**：[https://kyleexu.github.io/novena](https://kyleexu.github.io/novena)

## 📁 项目结构

```
novena/
├── project/          # 实际项目经验总结
│   ├── market/       # 行情系统（6篇）
│   ├── otc/          # OTC 交易系统（2篇）
│   ├── rate-limit/   # 分布式限流（3篇）
│   └── rule-engine/  # 规则引擎（1篇）
├── repository/       # 技术栈知识库
│   ├── flink/        # Flink 流计算（1篇）
│   ├── java/         # Java 核心（5篇）
│   ├── kafka/        # Kafka 消息队列（2篇）
│   ├── mysql/        # MySQL 数据库（3篇）
│   ├── redis/        # Redis 缓存（2篇）
│   └── others/       # 其他技术（5篇）
├── english/          # 英文技术文档与面试准备
│   ├── market/       # 行情系统英文表达（6篇）
│   ├── rule-engine/  # 规则引擎英文表达（1篇）
│   └── vocabulary/   # 技术词汇表（19篇）
├── interview/        # 面试总结（1篇）
└── resume/           # 个人简历
    ├── en/          # 英文简历
    └── zh/          # 中文简历
```

---

## 🚀 项目经验 (project/) — 12篇

### 💹 行情系统 (market/) — 6篇

基于 Kafka + Flink 构建的交易所实时行情推送系统，通过 MQTT 实现毫秒级推送。

| 文档 | 内容描述 |
|------|----------|
| [01. 系统结构](project/market/01.%20系统结构.md) | 整体架构设计，四条主要数据流 |
| [02. Flink 任务](project/market/02.%20Flink%20任务.md) | TickerJob、CandleJob、OrderbookJob 详解 |
| [03. 推送技术选型](project/market/03.%20推送技术选型.md) | MQTT vs WebSocket 深度对比 |
| [04. 价格偏差处理](project/market/04.%20价格偏差处理.md) | 价格计算与偏差控制策略 |
| [05. K 线补偿](project/market/05.%20K%20线补偿.md) | 数据缺失场景的补偿机制 |
| [06. MQTT 耗时分析](project/market/06.%20MQTT%20耗时分析.md) | 端到端延迟分析与优化 |

**核心技术**：Kafka · Flink · MQTT · Redis · WebSocket

### 🏪 OTC 系统 (otc/) — 2篇

场外交易系统的订单生命周期管理与结算流程。

- [01. 订单状态](project/otc/01.%20订单状态.md) - 订单状态机设计
- [02. OTC 结算](project/otc/02.%20OTC%20结算.md) - 结算流程设计

**核心技术**：状态机 · 分布式事务

### 🚦 限流系统 (rate-limit/) — 3篇

分布式限流方案设计与实现。

- [01. 概况](project/rate-limit/01.%20概况.md) - 限流方案概述
- [02. 同一毫秒多次请求](project/rate-limit/02.%20同一毫秒多次请求.md) - 高并发场景处理
- [03. 与单机限流比](project/rate-limit/03.%20与单机限流比.md) - 分布式 vs 单机方案

**核心技术**：Redis · Lua · 滑动窗口

### ⚙️ 规则引擎 (rule-engine/) — 1篇

业务规则引擎架构设计。

- [01. 概述](project/rule-engine/01.%20概述.md) - 规则引擎架构

**核心技术**：规则引擎 · 业务建模

---

## 📚 技术知识库 (repository/) — 18篇

### ⚡ Flink — 1篇
- [01. flink-architecture](repository/flink/01.%20flink-architecture.md) - 架构原理与核心概念

### ☕ Java — 5篇
- [01. concurrent mark sweep](repository/java/01.%20concurrent%20mark%20sweep.md) - CMS 垃圾收集器
- [02. G1](repository/java/02.%20G1.md) - G1 垃圾收集器
- [03. hashmap](repository/java/03.%20hashmap.md) - HashMap 底层实现
- [04. concurrenthashmap](repository/java/04.%20concurrenthashmap.md) - 并发容器原理
- [05. lock & synchornized](repository/java/05.%20lock%20&%20synchornized.md) - 锁机制对比

### 📨 Kafka — 2篇
- [01. 结构](repository/kafka/01.%20结构.md) - Broker、Topic、Partition
- [02. 丢失、重复与有序](repository/kafka/02.%20丢失、重复与有序.md) - 消息可靠性保证

### 🗄️ MySQL — 3篇
- [01. 并发修改](repository/mysql/01.%20并发修改.md) - 乐观锁与悲观锁
- [02. 死锁](repository/mysql/02.%20死锁.md) - 死锁场景分析与解决
- [03. mvcc](repository/mysql/03.%20mvcc.md) - 多版本并发控制

### 🔴 Redis — 2篇
- [01. 数据结构](repository/redis/01.%20数据结构.md) - 五大数据类型底层实现
- [02. 分布式锁](repository/redis/02.%20分布式锁.md) - Redisson 实现方案

### 🔧 其他技术 — 5篇
- [01. nonce 与时间戳](repository/others/01.%20nonce%20与时间戳.md) - 防重放攻击
- [02. 状态机](repository/others/02.%20状态机.md) - 状态机设计模式
- [03. 事件驱动](repository/others/03.%20事件驱动.md) - 事件驱动架构
- [04. 高性能的架构](repository/others/04.%20高性能的架构.md) - 高并发系统设计
- [05. 零拷贝](repository/others/05.%20零拷贝.md) - 零拷贝技术原理

---

## 🌍 英文面试准备 (english/) — 27篇

### 🙋‍♂️ 自我介绍 — 1篇
- [self-introduction](english/self-introduction.md) - 英文自我介绍模板

### 📈 行情系统 (Market System) — 6篇
| 文档 | 内容 |
|------|------|
| [01-system-architecture](english/market/01-system-architecture.md) | 系统架构英文表达 |
| [02-mqtt-vs-websocket](english/market/02-mqtt-vs-websocket.md) | 技术选型讨论 |
| [03-parallel-vs-serial](english/market/03-parallel-vs-serial.md) | 并行与串行处理 |
| [04-technical-points](english/market/04-technical-points.md) | 核心技术点 |
| [05-price-deviation-controls](english/market/05-price-deviation-controls.md) | 价格偏差控制 |
| [06-latency-analysis](english/market/06-latency-analysis.md) | 延迟分析 |

### ⚙️ 规则引擎 (Rule Engine) — 1篇
- [01. summary](english/rule-engine/01.%20summary.md) - 规则引擎概述

### 📖 技术词汇表 (vocabulary/) — 19篇

按主题系统化整理的技术英语词汇：

| 编号 | 主题分类 | 编号 | 主题分类 |
|------|----------|------|----------|
| [01](english/vocabulary/subject/01-basic-computer-vocabulary.md) | 基础计算机词汇 | [11](english/vocabulary/subject/11-java-ecosystem.md) | Java 生态 |
| [02](english/vocabulary/subject/02-programming-language-core.md) | 编程语言核心 | [12](english/vocabulary/subject/12-spring-framework.md) | Spring 框架 |
| [03](english/vocabulary/subject/03-data-structures-algorithms.md) | 数据结构与算法 | [13](english/vocabulary/subject/13-system-design.md) | 系统设计 |
| [04](english/vocabulary/subject/04-operating-system-network.md) | 操作系统与网络 | [14](english/vocabulary/subject/14-performance-optimization.md) | 性能优化 |
| [05](english/vocabulary/subject/05-database.md) | 数据库 | [15](english/vocabulary/subject/15-devops-deployment.md) | DevOps |
| [06](english/vocabulary/subject/06-distributed-systems.md) | 分布式系统 | [16](english/vocabulary/subject/16-software-engineering-practices.md) | 软件工程 |
| [07](english/vocabulary/subject/07-microservices.md) | 微服务 | [17](english/vocabulary/subject/17-testing.md) | 测试 |
| [08](english/vocabulary/subject/08-message-queue.md) | 消息队列 | [18](english/vocabulary/subject/18-security.md) | 安全 |
| [09](english/vocabulary/subject/09-caching.md) | 缓存 | [19](english/vocabulary/subject/19-interview-expressions.md) | 面试表达 |
| [10](english/vocabulary/subject/10-concurrency-multithreading.md) | 并发与多线程 |  |  |

---

## 📄 面试总结 (interview/) — 1篇

- [summary](interview/summary.md) - 面试经验总结

---

## 📝 个人简历 (resume/)

### Markdown 简历
- [markdown-resume](resume/markdown-resume.md) - Markdown 格式简历

### LaTeX 简历
- **中文版**：[kyle_resume_zh.tex](resume/zh/kyle_resume_zh.tex)
- **英文版**：[kyle_resume_en.tex](resume/en/kyle_resume_en.tex)

---

## 🎯 技术栈总览

| 分类 | 技术 |
|------|------|
| **语言** | Java |
| **框架** | Spring Boot, Spring Cloud |
| **消息队列** | Kafka, MQTT |
| **流计算** | Flink |
| **数据库** | MySQL |
| **缓存** | Redis |
| **协议** | WebSocket, MQTT |

---

## 📊 统计信息

| 类别 | 文档数量 | 说明 |
|------|----------|------|
| **项目经验** | 12篇 | 真实业务场景的技术方案 |
| **技术知识库** | 18篇 | 核心技术栈深度总结 |
| **英文面试** | 27篇 | 技术英语表达与词汇 |
| **面试总结** | 1篇 | 面试经验整理 |
| **简历模板** | 3篇 | 中英文简历模板 |
| **总计** | **61篇** | 系统化技术知识体系 |

---

## 🔧 本地预览

```bash
# 安装 docsify-cli
npm i docsify-cli -g

# 启动本地服务
docsify serve .

# 访问 http://localhost:3000
```

---

## 🌟 推荐阅读路线

### 🎯 项目经验学习路线
1. **行情系统**：01 系统结构 → 02 Flink 任务 → 03 推送技术选型
2. **深度技术**：价格偏差处理 → MQTT 耗时分析 → K线补偿

### 📚 技术知识库学习路线
1. **Java 基础**：HashMap → ConcurrentHashMap → 锁机制
2. **分布式系统**：Kafka 可靠性 → Redis 分布式锁 → 高性能架构
3. **数据库**：MVCC → 死锁分析 → 并发控制

### 🌍 英文面试准备路线
1. **基础准备**：自我介绍 → 基础计算机词汇 → 编程语言核心
2. **项目表达**：系统架构 → 技术要点 → 面试表达
3. **深度主题**：分布式系统 → 性能优化 → 系统设计

---

## 📜 License

本项目仅用于个人学习和技术分享。

---

**Last Updated:** March 2026
# 问数机器人-测试题

## 1. 数据集

### 1.1 构建数据库

#### 1.1.1 Install Just

* macOS ```brew install just```
* Ubuntu ```apt install just```

#### 1.1.2 启动数据库

构建数据库：```just up```

* 预览数据库：`http://localhost:8080`, db password:`winwin1234`

> 提示: `.env.example` to `.env`

* 测试数据库：```just test```
* 关闭数据库：```just down```

### 1.2 数据表介绍

* dim_category（类目维表）
* dim_product （商品维表）
* product_sales_monthly （商品月度销售表）
    * 时间维度<biz_date>：2023年1月份至2025年5月份的销售数据。
    * 地理维度：
        * 大区<region_name>：包括华北地区,华东地区,西南地区,西北地区,华南地区,华中地区,东北地区,NULL。（NULL：代表全国）
        * 省份<province_name>：包括24个省,NULL。（NULL：代表全国）
  > 所以，当大区和省份同时为NULL时，才代表是全国。
    * 业态维度<channel>：包括大卖场,大超市,小超市,便利店,食杂店,NULL。（NULL：代表全业态）
  > 所以，当业态为NULL时，才代表是全业态。

## 2. Text2SQL任务

上面脚本已经构建本地Postgres数据库。请基于此数据库表，完成一个RAG数据问答机器人。

1. `docs/examples.yml` 有部分SQL示例。
2. `docs/instruction.md` 是一些指标描述。
3. `docs/test.csv` 是需要完成的**测试问题**。

> （问题描述为`数据库问题`，必须进行查询数据库来回答）。

技术实现需要完成以下功能 Pipes（可自行设计添加其他pipe）:

* Question Router（必须）
* Question Annotation（可选）
* SQL Generator（必须）
* SQL Correction（可选）
* SQL Executor（必须）
* Answer Summary（可选）

**技术框架不限。保留实现方案的思考逻辑，迭代方向。**

## 3. 评分标准

* RAG基础 🌟🌟🌟
* COT思维 🌟
* Pipeline设计能力 🌟🌟
* 工程化编码能力 🌟🌟

## 4. 结果要求

* 编程语言：Python优先、Typescript/Go均可。
* 测试问题: 要求至少可回答这些问题`(docs/test.csv)`
* 保留完整的代码实现，提供一个HTTP服务、或者可以被方便调用的Lib，注明使用方式。
* 【加分项】记录你的对项目实现的思路、实现经历、可继续优化的方向的描述。

## 5. 提交方式

* 克隆仓库，打包完整项目Zip，发给HR。
* 或者Fork项目（不要提PR），提交你的仓库链接，发给HR。
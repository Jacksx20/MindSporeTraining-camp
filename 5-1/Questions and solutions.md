# 单节点数据缓存模块

MindSpore新特性介绍单节点数据缓存

- Cache_server如何启动

​        Cache Server的服务由一个外部守护进程提供，在使用Cache服务前，要先在Mindspore外部启动一个服务器守护进程，来与缓存客户进行交互沟通

```bash
ms_cache_server start|session [–m <mem_size>] [-d <spill_path>] [-nospill] [-h <host>] [-p <port>]

Command: start | session

start
– starts the service

session
– creates a new caching session, returning the session_id as output

```



- cache_server创建时默认的port端口号

​        默认值:50052



- cache_client实体在创建时，其<session_id>如何获取

  ​     唯一标识与缓存服务的连接d session。应该从ms_cache_service session命令返回的session_id。当给出该选项时，缓存的大小和溢出行为取自session。如果未给出值，则假设这是唯一的通道，没有其他通道将共享此缓存。在这种情况下，将自动生成一个session_id。

  ```shell
  ms_cache_server session –h host –p port –m memsize
  ```


# 单节点数据缓存模块

MindSpore新特性介绍单节点数据缓存

- Cache_server如何启动

​        Cache Server的服务由一个外部守护进程提供，在使用Cache服务前，要先在Mindspore外部启动一个服务器守护进程，来与缓存客户进行交互沟通

```shell
ms_cache_server start|session [–m <mem_size>] [-d <spill_path>] [-nospill] [-h <host>] [-p <port>]


#Command: start | session

#start
#– starts the service
#
#session
#– creates a new caching session, returning the session_id as output

```

​      然后启动

```shell
cache_admin --start
```

![启动服务](%E5%90%AF%E5%8A%A8%E6%9C%8D%E5%8A%A1.png)

- cache_server创建时默认的port端口号

​        默认值:50052



- cache_client实体在创建时，其<session_id>如何获取

  ​     唯一标识与缓存服务的连接session。应该从ms_cache_service session命令返回的session_id。当给出该选项时，缓存的大小和溢出行为取自session。如果未给出值，则假设这是唯一的通道，没有其他通道将共享此缓存。在这种情况下，将自动生成一个session_id。

  ```shell
  ms_cache_server session –h host –p port –m memsize
  ```

​             若缓存服务器中不存在缓存会话，则需要创建一个缓存会话，得到缓存会话id：

![创建Session](%E5%88%9B%E5%BB%BASession.png)





笔记：https://bbs.huaweicloud.com/forum/thread-105575-1-1.html
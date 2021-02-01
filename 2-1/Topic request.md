# MindSporeLite

华为智慧终端背后的黑科技----超轻量AI引擎MindSpore Lite

2-1在 MindSpore model_zoo下载模型mobilenetv2.mindir（[https://download.mindspore.cn/model_zoo/official/lite/mobilenetv2_openimage_lite](https://download.mindspore.cn/model_zoo/official/lite/mobilenetv2_openimage_lite) ）, 使用MindSpore lite converter 转成.ms 模型，请保留所使用的模型转换命令和模型转换截图



将.mindir模型转换为.ms 模型

```bash
call converter_lite --fmk=MINDIR --modelFile=c:\Users\Administrator\Desktop\MindSporePetClassification\converter\mobilenetv2.mindir --outputFile=Jack20
```

   注意：其中c:\Users\Administrator\Desktop\MindSporePetClassification\converter\mobilenetv2.mindir代表生成的mindir文件，而--outputFile定义转换后MS文件的名称。

成功后，会在converter文件夹中生成对应的.ms文件。



笔记：https://bbs.huaweicloud.com/forum/thread-105116-1-1.html
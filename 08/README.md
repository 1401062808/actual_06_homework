# 第八次课作业


## 把第七次课的作业功能前端不刷新页面完成


* 用户名密码，实现添加和删除的功能
* 不刷新页面，使用ajax完成

    - 提示，如果一个按钮是异步生成的，一开始绑定的时间就失效了，需要改一下写法

```
$('.test').on('click',function(){
    console.log(1)    
})

```



上面的代码，如果.test按钮不是页面初始化存在的，而是ajax异步渲染的，上面写法就会失效，需要用下面的代码

```
$(document).on('click','.test',function(){
    console.log(1)
})

```

用$(document).on，.test是第二个参数即可
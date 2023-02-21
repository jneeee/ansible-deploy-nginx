
## Ansible 部署一个 Nginx 代理两个后端

这是一个学习`ansible`的练手项目

实现一个用ansible**部署、管理、测试**的 front haproxy\*1, backend nginx\*2的七层负载业务。
项目旨在熟悉ansible及其各种特性概念 `role, inventory, host vars, library, template` 等等。部分步骤有其他更简单的完成方式，比如把deploy_nginx抽象成一个role这步，直接在dockerfile中实现更简单。某些概念如果理解有误欢迎指正。

![](/pic/bp.png)

文件夹介绍：
- `ansible_pb/` ansible playbook
- `build_image/` 用来生成镜像和容器

前提条件，本地有如下软件：
- docker
- python2

```bash
git clone git@github.com:jneee/study_ansible.git
cd ansible_pb
ansible-playbook container_init.yml
ansible-playbook deploy_nginx.yml
ansible-playbook deploy_haproxy.yml
ansible-playbook add_backend.yml --extra-vars "new_ip=11.2.0.4" 
# Todo 新加后端的IP没有持久化保存到本地
ansible-playbook operate_all_backend_by_tags.yml --tags "start_nginx|stop_nginx|reload_nginx"
# 访问haproxy地址100次，查看回显统计是否正常（回显是container_id前12位），如下图
ansible-playbook check_lb_res.yml
ansible-playbook undeploy.yml
```

测试结果：（一共访问100次，每个后端ID都被访问了50次）

![](/pic/test_res.png)


## Todo

- 安装时候自己起个repo server 
- tags
- include_tasks/import_tasks 区别


from invoke import task


@task
def test(c):
    """
    invoke task test function
    :param c:
    :return:
    """
    print('hello, this is a test invoke demo.')


@task(help={'name': 'A param for test'})
def hello(c, name):
    """
    invoke task test function receive one param
    :param c:
    :param name:
    :return:
    """
    c.run(f"echo {name} 加油！")


@task()
def deploy(c):
    """
    deploy fastapi service
    :param c:
    :return:
    """
    # print('正在启动服务')
    c.run(f'poetry run python worker.py')
    # print('服务启动成功')

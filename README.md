# Test-uv-index

测试使用 `[tool.uv.index]` 来配置 Python 镜像源。<br>

以及测试多 index 的用例:<br>

```toml
dependencies = [
     "numpy==1.26.4",
     "matplotlib==3.10.0"
]
[[tool.uv.index]]
name = "tsinghua"
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
explicit = true

[[tool.uv.index]]
name = "aliyun"
url = "https://mirrors.aliyun.com/pypi/simple/"
explicit = true

[tool.uv.sources]
numpy = [
      { index = "tsinghua"},
]

matplotlib = [
      { index = "aliyun"}
]
```

这里用了清华和阿里源。<br>

## 运行:

```shell
uv venv -p 3.10
uv pip install git+https://github.com/MrXnneHang/test-uv-index.git
uv run test-uv
```


很多时候你需要多个 index。比如对于 torch 的特定版本安装。它的`cpu`,`cu11`,`c12`等不同 wheel 存放在特定 index-url 中。<br>

更多参见: [【tool.uv.index】 使用 uv 配置依赖于 Pytorch 的 pyproject 并单独配置针对cpu或cuda版本.](https://xnnehang.top/blog/202)。<br>
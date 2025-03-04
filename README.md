# Test-uv-index

测试使用 `[tool.uv.index]` 来配置 Python 镜像源。<br>

以及测试多 index 的用例:<br>

```toml
[[tool.uv.index]]
# Optional name for the index. 这个可以不写
name = "tsinghua"
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
default = true

[[tool.uv.index]]
name = "aliyun"
url = "https://mirrors.aliyun.com/pypi/simple/"
```

改用了清华源作为默认源，并且添加了阿里源作为备选。并且由于 defualt 选项， `pypi`被排除了。<br>

## 运行:

```shell
uv venv -p 3.10
uv pip install git+https://github.com/MrXnneHang/test-uv-index.git
uv run test-uv
```
如果成功运行，它会打印`numpy`,`matplotlib`版本并且在工作目录保存一张图片。<br>

很多时候你需要多个 index。比如对于 torch 的特定版本安装。它的`cpu`,`cu11`,`c12`等不同 wheel 存放在特定 index-url 中。<br>

更多参见: 
- [Dive Into [tool.uv.index] 为 uv 配置 Python 镜像源。| 排除pypi | explicit和default参数,以及None参数](https://xnnehang.top/blog/203)
- [【tool.uv.index】 使用 uv 配置依赖于 Pytorch 的 pyproject 并单独配置针对cpu或cuda版本.](https://xnnehang.top/blog/202)。<br>
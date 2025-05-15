# Test-uv-index

这是一个 [tool.uv.index] 的使用样例, 包含:

- 使用清华源替换 pypi 作为默认源
- 使用南京源下载 torch-cpu

```toml
[[tool.uv.index]]
# Optional name for the index. 这个可以不写
name = "tsinghua"
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
default = true

[[tool.uv.index]]
name = "torch-cpu-nju"
url = "https://mirror.nju.edu.cn/pytorch/whl/cpu/"
explicit = true

[tool.uv.sources]
torch = [
  { index = "torch-cpu-nju" },
]
```

还有一些值得注意的地方, 比如, 每个 torch 一般都只支持两个 python 版本, 所以你应该及时约束避免别人默认安装时报错:

```shell
➜  test-uv-index git:(master) ✗ uv run test-uv   
Using CPython 3.13.0
Creating virtual environment at: .venv
error: Distribution `torch==2.1.0+cpu @ registry+https://mirror.nju.edu.cn/pytorch/whl/cpu/` can't be installed because it doesn't have a source distribution or wheel for the current platform
```

## 运行:

```shell
git clone https://github.com/MrXnneHang/test-uv-index.git    
cd test-uv-index
uv run test-uv
```
如果成功运行，你应该会看到:

```shell
➜  test-uv-index git:(master) ✗ uv run test-uv
Using CPython 3.11.11
Removed virtual environment at: .venv
Creating virtual environment at: .venv
      Built test-uv-index @ file:///home/xnne/code/test-uv-index
Installed 21 packages in 236ms
matplotlib:3.10.1
numpy:1.26.4
torch:2.1.0+cpu
torch cuda available:False
tensor([ 0.0000e+00,  6.3424e-02,  1.2659e-01,  1.8925e-01,  2.5115e-01,
         3.1203e-01,  3.7166e-01,  4.2979e-01,  4.8620e-01,  5.4064e-01,
         5.9291e-01,  6.4279e-01,  6.9008e-01,  7.3459e-01,  7.7615e-01,
         8.1458e-01,  8.4973e-01,  8.8145e-01,  9.0963e-01,  9.3415e-01,
         9.5490e-01,  9.7181e-01,  9.8481e-01,  9.9384e-01,  9.9887e-01,
         9.9987e-01,  9.9685e-01,  9.8982e-01,  9.7880e-01,  9.6384e-01,
         9.4500e-01,  9.2235e-01,  8.9599e-01,  8.6603e-01,  8.3257e-01,
         7.9576e-01,  7.5575e-01,  7.1269e-01,  6.6677e-01,  6.1816e-01,
         5.6706e-01,  5.1368e-01,  4.5823e-01,  4.0093e-01,  3.4202e-01,
         2.8173e-01,  2.2031e-01,  1.5800e-01,  9.5056e-02,  3.1728e-02,
        -3.1728e-02, -9.5056e-02, -1.5800e-01, -2.2031e-01, -2.8173e-01,
        -3.4202e-01, -4.0093e-01, -4.5823e-01, -5.1368e-01, -5.6706e-01,
        -6.1816e-01, -6.6677e-01, -7.1269e-01, -7.5575e-01, -7.9576e-01,
        -8.3257e-01, -8.6603e-01, -8.9599e-01, -9.2235e-01, -9.4500e-01,
        -9.6384e-01, -9.7880e-01, -9.8982e-01, -9.9685e-01, -9.9987e-01,
        -9.9887e-01, -9.9384e-01, -9.8481e-01, -9.7181e-01, -9.5490e-01,
        -9.3415e-01, -9.0963e-01, -8.8145e-01, -8.4973e-01, -8.1458e-01,
        -7.7615e-01, -7.3459e-01, -6.9008e-01, -6.4279e-01, -5.9291e-01,
        -5.4064e-01, -4.8620e-01, -4.2979e-01, -3.7166e-01, -3.1203e-01,
        -2.5115e-01, -1.8925e-01, -1.2659e-01, -6.3424e-02, -2.4493e-16],
       dtype=torch.float64)
```

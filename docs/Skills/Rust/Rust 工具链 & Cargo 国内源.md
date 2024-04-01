# Rust 工具链 & Cargo 国内源

使用阿里源

> https://developer.aliyun.com/mirror/rustup

## rustup

Install

```bash
# 使用阿里云安装脚本
curl --proto '=https' --tlsv1.2 -sSf https://mirrors.aliyun.com/repo/rust/rustup-init.sh | sh
```

rustup:

```
export RUSTUP_UPDATE_ROOT=https://mirrors.aliyun.com/rustup/rustup
export RUSTUP_DIST_SERVER=https://mirrors.aliyun.com/rustup
```

## Cargo

> https://rust-guide.niqin.com/en-us/4-cargo/4.1-source-replacement.html

> Cargo 配置文件：`$CARGO_HOME/config.toml`
> - Windows:
>   - `%USERPROFILE%\.cargo\config.toml`
> - Unix:
>   - `$HOME/.cargo/config.toml`

目前该镜像仅支持稀疏索引配置，需要您的 cargo 版本 >=1.68。修改配置文件，如下：

```config
[source.crates-io]
replace-with = 'aliyun'
[source.aliyun]
registry = "sparse+https://mirrors.aliyun.com/crates.io-index/"
```

PS:

其他可用源：

```
[source.crates-io]
replace-with = 'aliyun'
[source.aliyun]
registry = "sparse+https://mirrors.aliyun.com/crates.io-index/"
```

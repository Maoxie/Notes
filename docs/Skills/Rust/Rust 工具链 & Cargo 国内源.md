# Rust 工具链 & Cargo 国内源

rustup:
> https://rust-guide.niqin.com/en-us/3-env/3.1-rust-toolchain-cn.html

## Cargo

> https://rust-guide.niqin.com/en-us/4-cargo/4.1-source-replacement.html

> Cargo 配置文件：`$CARGO_HOME/config.toml`
> - Windows:
>   - `%USERPROFILE%\.cargo\config.toml`
> - Unix:
>   - `$HOME/.cargo/config.toml`

修改配置文件，如下：

```config
[source.crates-io]
registry = "https://github.com/rust-lang/crates.io-index"
replace-with = 'sjtu' # pick one of the following source

[source.ustc]
registry = "sparse+https://mirrors.ustc.edu.cn/crates.io-index/"

[source.sjtu]
registry = "sparse+https://mirrors.sjtug.sjtu.edu.cn/git/crates.io-index/"

[source.tuna]
registry = "sparse+https://mirrors.tuna.tsinghua.edu.cn/crates.io-index/"

[source.rustcc]
registry = "sparse+https://code.aliyun.com/rustcc/crates.io-index/"
```

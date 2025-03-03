# 附录: 相关资源

本附录对文档中提到的资源进行整理和说明。

## 活动说明

- [全国大学生计算机系统能力大赛](https://os.educg.net/#/)：即文档中提到的 OS 比赛，其中的操作系统内核实现赛道包含了一系列内核测例，可以验证内核自身的功能和性能。

## 代码仓库

### 原始代码仓库

- [arceos-org/arceos](https://github.com/arceos-org/arceos)：ArceOS 是由清华大学贾越凯博士开发的组件化操作系统。它本身是一个 Unikernel 架构的操作系统，可以支持宏内核、hypervisor 等架构的扩展，是本毕设的基础前置工作。

- [Starry-OS/Starry-Old](https://github.com/Starry-OS/Starry-Old)：Starry 是基于 ArceOS 开发的宏内核，参与全国大学生操作系统大赛并通过了决赛阶段的绝大部分测例。

- [arceos-org/starry-next](https://github.com/arceos-org/starry-next)：Starry-Next 是 Starry 的下一代版本，它将对 Starry 进行重构，以较小的代码量实现更加完善的宏内核功能，验证组件化开发的优势和可行性，是本毕设的主要目标。该仓库是上游稳定仓库，更新较慢。

### 衍生代码仓库

- [oscomp/arceos](https://github.com/oscomp/arceos)：ArceOS 适配到 OS 比赛的衍生仓库。该仓库为 ArceOS 添加了各类 OS 比赛所需的支持，包括 loongarch64 指令集架构支持、新的功能接口等，并会在将来逐渐合入到上游仓库中，也是本毕设的主要工作仓库。

- [oscomp/starry-next](https://github.com/oscomp/starry-next)：Starry-Next 适配到 OS 比赛的衍生仓库。该仓库为 Starry-Next 添加了各类 OS 比赛所需的支持，包括 loongarch64 指令集架构支持、新的功能接口等，并会在将来逐渐合入到上游仓库中，也是本毕设的主要工作仓库。

## 相关说明文档

Starry 的相关说明文档详见 [Starry-Tutorial-Book](https://azure-stars.github.io/Starry-Tutorial-Book/)。
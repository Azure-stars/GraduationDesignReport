# dependencies-patch
## dependencies-patch::git_patch
 此包位于dependencies-patch::git_patch，主要功能是处理Git补丁的相关信息，特别是Git仓库名称、包重命名信息、补丁版本以及补丁目标的具体信息。它包含一个名为`GitPatch`的结构体，该结构体包含了以下字段：

- `git`: String, 表示Git仓库名称。
- `package`: Option<String>, 可能包含包的重命名信息。
- `version`: Option<String>, 补丁版本信息。
- `info`: GitInfo, 补丁目标信息。

关键类型：
    - `GitPatch`：一个结构体，包含了Git仓库名称、包重命名信息、补丁版本以及补丁目标的具体信息。
    - `GitInfo`：一个枚举类型，用于表示Git仓库的信息。它包含以下几种变体：
        - `None`: 没有特定的信息。
        - `Commit(String)`: 提交哈希值，表示一个具体的提交。
        - `Tag(String)`: 标签名称，表示一个具体的标签。
        - `Branch(String)`: 分支名称，表示一个具体的分支。
    - `String`：字符串类型，用于表示文本数据。
    - `Option`：枚举类型，用于表示可能存在的值或可能缺失的值。它有两个变体：Some(T)和None。

此包通过提供结构化的Git补丁信息处理机制，确保了在复杂的Git操作中能够准确地管理和使用补丁相关的元数据，为应用中的版本控制和补丁管理提供了便利。
### Functions
#### check_git_patch_format
CheckGitPatchFormat函数用于检查给定的Git补丁是否符合正确的格式，即仓库名称应为`owner/repo`的形式。

入参：
- patch: 一个指向GitPatch类型的指针。

出参：
- Ok((owner, repo)): 如果补丁的仓库名称格式正确，返回仓库的所有者和仓库名。
- Err(mes): 如果补丁的仓库名称格式不正确，返回错误信息。

主要执行流程：
1. 将补丁的仓库名称按`/`分割成一个字符串向量。
2. 检查向量的长度是否为2。
3. 如果是2，则将第一个元素作为所有者，第二个元素作为仓库名，返回Ok((owner, repo))。
4. 如果长度不为2，则根据补丁的仓库名称生成错误信息并返回Err(mes)。
#### GitPatch::new
Create a new git patch with specific information including the repository name, optional package and version names, and detailed GitInfo.
#### do_git_patch
###
### Vars
#### git_table
`git_table` 是一个变量，它从 `patch_toml_table` 中获取一个可变的 TOML 表。
#### real_package_name
`real_package_name` 是一个变量，用于在给定包名不存在时，回退到默认的包名。它在代码中通过匹配操作来决定其值：

- 如果存在一个名为 `patch.package` 的可选包名（Some(name)），则使用该名称。
- 否则，使用预定义的全局变量 `package_name`。

这个变量主要用于处理包名的选择逻辑，确保在任何情况下都能获取到一个有效的包名。
#### (mut toml_table, package_index)
`tolm_table` 是一个可变的全局变量，主要用于处理TOML格式的配置表。它与 `gen_patch_table` 函数和 `package_index` 相关联。

`toml_table` 的主要功能是从指定的路径读取并解析一个TOML文件，获取名为 "patch" 的表，并将其转换为可变表。如果操作成功，则返回该表；否则，程序将终止执行。
#### patch_toml_table
`patch_toml_table`是一个变量，用于获取并操作一个TOML表中的“patch”部分。该变量主要功能是提供对特定TOML表格的修改能力。
#### patch_git
`patch_git`是一个字符串变量，用于存储从给定的命名参数构造的Git仓库URL。

它主要关联的主要函数是`format!`，用于格式化字符串。
#### mut file
`file` 是一个变量，主要功能是作为文件句柄，用于对指定路径下的 `Cargo.toml` 文件进行追加操作。该变量关联的主要函数或类型是 `OpenOptions` 结构体，它用于配置文件系统的打开选项。具体来说：

- `OpenOptions::new()` 创建一个新的 `OpenOptions` 实例，用于设置各种打开选项。
- `.append(true)` 设置追加模式为 true，表示在写入数据时将内容添加到文件末尾。
- `.open(format!("{}/Cargo.toml", cargo_path))` 根据给定的路径格式化字符串并尝试以追加模式打开文件。如果路径不存在或无法打开，程序将抛出 `panic`。
- `.unwrap()` 用于处理可能的错误情况，确保程序在遇到错误时不会崩溃。
#### mut patch_table
`patch_table`是一个可变变量，初始化为一个新的`Table`实例。它主要用于存储补丁信息或配置表数据。
#### names
`names`是一个字符串数组变量，用于存储路径分隔后的名称。它主要在Git相关的操作中使用。
## dependencies-patch::cargo_parse
 此包位于dependencies-patch::cargo_parse，专注于解析Cargo Package中的依赖关系，特别是处理source字段为Git仓库或注册表的依赖项。主要功能如下：

关键函数：
    - CargoPackage.parse_dependency: 该函数用于将Cargo Package中的source字段解析为Dependency类型。其主要功能包括：
        1. 检查source是否以“git+”开头，如果是，则提取出Git仓库URL。
        2. 如果找到问号（?），则截取到问号前的部分作为Git地址；否则，直接使用整个字符串作为Git地址。
        3. 如果source以“registry+”开头，则返回一个默认的注册表信息Dependency::Registry("crates-io".to_string())。
        4. 如果source既不以“git+”也不以“registry+”开头，则调用panic!函数终止程序并报告错误。

此包通过提供对依赖项来源的有效解析，确保了项目在处理Git仓库或注册表时的准确性和可靠性，避免了潜在的错误和不确定性。
### Functions
#### CargoPackage.parse_dependency
解析依赖函数用于将CargoPackage中的source字段解析为Dependency类型。该函数主要功能如下：

1. 检查source是否以“git+”开头，如果是，则提取出Git仓库URL。
2. 如果找到问号（?），则截取到问号前的部分作为Git地址；否则，直接使用整个字符串作为Git地址。
3. 如果source以“registry+”开头，则返回一个默认的注册表信息Dependency::Registry("crates-io".to_string())。
4. 如果source既不以“git+”也不以“registry+”开头，则调用panic!函数终止程序并报告错误。
#### pick_package
pick_package函数用于从指定的Cargo路径中选择特定的包。主要功能包括：检查Cargo.toml和Cargo.lock文件是否存在，如果不存在则生成新的Cargo.lock文件；解析Cargo.lock文件以查找指定名称的包并返回结果。

入参：
- cargo_path: 一个指向String类型的指针，表示Cargo项目的路径。
- package_name: 一个指向String类型的指针，表示要选择的包的名称。

主要执行流程：
1. 检查指定的Cargo路径下是否存在Cargo.toml文件，如果不存在则返回错误信息。
2. 获取Cargo.lock文件的路径，并检查其是否存在，如果不存在则记录警告日志并生成新的Cargo.lock文件。
3. 读取并解析Cargo.lock文件，查找指定名称的包，如果找不到则返回错误信息。
4. 返回找到的包或错误信息。
### Vars
#### output
`output`是一个变量，主要功能是用于执行系统命令。它关联的主要函数是`std::process::Command::new("cargo").arg("generate-lockfile").current_dir(cargo_path).spawn().expect(...)`，用于生成锁文件。这个命令接口包含几个方法，如`.arg()`用于添加参数，`.current_dir()`用于设置当前目录，以及`.spawn()`和`.wait()`用于执行命令并等待其完成。
#### cargo_toml_path
`cargo_toml_path`是一个字符串变量，用于表示Cargo项目的TOML文件路径。该路径是通过将`cargo_path`与字符串`"/Cargo.toml"`连接生成的。
#### git_url
`git_url` 是一个字符串变量，它的主要功能是从一个给定的源字符串中提取特定的部分。具体来说，它通过以下步骤从源字符串中提取URL：

1. 将源字符串按 `#` 分割成多个子字符串，形成一个向量。
2. 获取向量的第一个元素（即第一个子字符串）。
3. 如果该子字符串存在，则将其转换为字符串类型并进行下一步操作。
4. 从字符串中去掉前四个字符。

`git_url` 变量并未关联主要函数或类型，它仅用于简化对源字符串特定部分的提取和处理。
#### cargo_lock
cargo_lock是一个`CargoLock`类型的变量，主要功能是管理和定义依赖包的版本信息。它包含一个字段`package`，类型为`Vec<CargoPackage>`，用于存储多个依赖包的信息。
#### cargo_lock_path
`cargo_lock_path`是一个字符串变量，用于存储Cargo包管理工具的锁定文件路径。它的值是通过格式化操作生成的，具体格式为在`cargo_path`后面加上"/Cargo.lock"。该变量没有关联的主要函数或类型。
## dependencies-patch::arg_parse
 此包位于`dependencies-patch::arg_parse`，专注于为命令行工具提供修补Cargo依赖项的功能。它定义了一个名为`Args`的类型，这是一个结构体，用于配置如何修补Cargo依赖项。关键字段包括`cargo_path`、`package_name`、`patch_type`、`real_package_name`、`package_version`、`git_repo`、`commit`、`branch`、`tag`和`patch_path`，每个都有特定的用途。

关键类型：
    - Args: 一个结构体，用于配置修补Cargo依赖项的参数，包括项目路径、包名、修补类型以及具体的Git仓库信息或本地路径。

此包提供了一个简单的命令行工具接口，使用户能够指定项目路径和包名，并选择修补类型（如Git仓库、注册表或本地路径），从而实现依赖项的灵活修补。
### Functions
#### parse_args
`parse_args` 函数的主要功能是解析命令行参数。如果参数无效（例如，类型设置为 `git` 但 Git 仓库未提供），则返回 `None`。函数的主要步骤如下：

1. 使用 `Args::parse()` 解析命令行参数到 `Args` 结构体中。
2. 根据 `patch_type` 字段的值进行不同的验证和处理：
   - 如果 `patch_type` 是 `git`，则检查 `git_repo` 是否为空，如果不为空，进一步检查 `commit`、`branch` 和 `tag` 是否冲突。
   - 如果 `patch_type` 是 `path`，则检查 `patch_path` 是否为空。
   - 如果 `patch_type` 是 `registry`，则检查 `package_version` 是否为空。
   - 如果 `patch_type` 不支持，记录错误日志并返回 `None`。
3. 设置默认的 `cargo_path` 值（如果不存在的话）。
4. 返回解析后的参数 `Some(args)`。

该函数依赖以下类型：
- `Args`: 命令行工具的参数结构体，包含多种字段用于配置修补 Carg
### Vars
#### judge_array
`judge_array` 是一个数组变量，包含三个元素：`args.commit`、`args.branch` 和 `args.tag` 的引用。这个数组主要用于存储和传递相关信息，具体用途可能与代码中的分支判断、版本控制或其他逻辑处理有关。
#### mut args
`args`是一个可变变量，属于`Args`类型，主要功能是配置如何修补Cargo依赖项。`Args`类型是一个命令行工具的参数结构体，包含多个字段：`cargo_path`、`package_name`、`patch_type`、`real_package_name`、`package_version`、`git_repo`、`commit`、`branch`、`tag`和`patch_path`。该变量与命令行工具的参数解析功能相关联。
## dependencies-patch::logger
 这个包位于 dependencies-patch::logger，主要功能是提供日志记录服务。它不包含任何公开的函数、类型或变量。由于缺乏具体的功能描述和代码示例，无法详细总结其基本功能和用途。
### Functions
#### error_log
error_log宏的主要功能是将错误日志记录到指定的位置。

该函数的每个参数的意义：
- 无显式参数，因为这是一个宏（macro）而不是函数。
#### patch_error
该函数的主要功能是格式化错误信息并打印输出。它接受一个`std::fmt::Arguments`类型的参数，表示要格式化的字符串参数。函数的执行流程如下：

1. 使用`format!`宏将输入的`args`格式化为一个新的字符串`error`。
2. 调用`cprintln!`宏，该宏用于解析颜色标签并打印输出带颜色的文本。
3. `cprintln!`宏接受一个包含颜色和文本的TokenStream作为参数，这里使用了自定义的颜色标签来突出显示错误信息。
#### warn_log
该宏定义用于将警告日志记录到日志系统中。
入参：
- $($arg:tt)*: 可变数量的参数，表示要格式化的日志内容。
出参：无直接的出参，但调用了crate::logger::patch_warn函数进行实际的日志记录。
#### patch_warn
patch_warn函数用于格式化并打印警告信息。
入参：
- args: std::fmt::Arguments类型的参数，包含要打印的格式化字符串和参数。

主要执行流程：
1. 使用format宏将args转换为String类型，赋值给变量warn。
2. 调用cprintln宏，打印格式化的警告信息。
#### patch_info
该函数名为patch_info，用于格式化并打印信息。
入参：
- args: std::fmt::Arguments类型，表示要格式化的参数集合。

主要执行流程：
1. 使用format!宏将args参数进行格式化，生成一个字符串info。
2. 调用cprintln!宏，将格式化后的信息打印出来，前缀为<green><bold>[INFO]</bold></green>，后跟格式化的info内容。
#### info_log
该宏定义了一个名为`info_log`的日志记录宏，用于在代码中插入信息性日志。

主要功能和用途：
- `info_log!`宏提供了一种方便的方式来格式化并记录信息性日志消息。它将传入的参数进行格式化处理后，调用`crate::logger::patch_info`函数进行日志记录。

参数：
- 无直接参数（输入参数通过宏展开传递给`format_args!`）

主要执行流程：
1. `info_log!`宏接收任意数量和类型的输入参数。
2. 这些参数会被传递给`format_args!`函数进行格式化处理。
3. 格式化后的日志消息被传递给`crate::logger::patch_info`函数进行记录。
### Vars
#### info
`info`是一个字符串变量，主要功能是将格式化的字符串和参数组合在一起。这个变量关联的主要函数或类型是`format!`宏，用于将字符串与参数进行格式化拼接。
#### warn
`warn`是一个格式化字符串变量，主要功能是使用给定的参数进行格式化输出。

该变量关联的主要函数或类型没有具体提及。
#### error
`error`是一个格式化的错误信息字符串变量，使用Rust编程语言中的`format!`宏来生成。
## dependencies-patch::path_patch
 此包位于dependencies-patch::path_patch，专注于为包路径提供补丁信息的管理工具。关键函数：

- PathPatch::new(package string, path string) -> PathPatch: 使用提供的`package`和`path`参数创建一个新的PathPatch实例。该实例包含了初始化的`package`和`path`字段，用于表示可能被重命名的包名和补丁的目标路径。

关键类型：

- PathPatch: 是一个结构体，包含两个字段：
- package：一个可选的字符串类型，表示可能在Cargo.toml文件中被重命名的实际包名。
- path：一个字符串类型，表示补丁的目标路径。该类型主要功能是提供对包路径的详细描述，以便在构建系统或版本控制系统中进行管理和调整。
### Functions
#### do_path_patch
do_path_patch函数的主要功能是将特定包的信息插入到Git仓库的Cargo.toml文件中。

入参：
- cargo_path: 一个指向String类型的指针，表示Cargo项目的路径。
- package_name: 一个指向String类型的指针，表示要选择的包的名称。
- patch: 一个PathPatch结构体，包含补丁信息。

主要执行流程：
1. 根据patch中的package字段或默认使用package_name来确定实际的包名（real_package_name）。
2. 调用gen_patch_table函数生成补丁表，如果生成失败则直接返回。
3. 从补丁表中获取与指定包相关的索引（package_index）。
4. 初始化一个空的补丁表（patch_table）并插入path信息。
5. 将补丁表插入到Cargo.toml文件中，以追加模式打开文件并在文件末尾写入补丁内容。

主要依赖函数：
- gen_patch_table: 生成补丁表，用于在Cargo.toml文件中插入或更新补丁信息。
#### PathPatch::new
PathPatch结构体用于表示对包路径的补丁信息，主要功能包括：
- 提供一个可选的字符串类型字段`package`，表示可能在Cargo.toml文件中被重命名的实际包名。
- 提供一个字符串类型字段`path`，表示补丁的目标路径。

该结构体的主要执行流程如下：
1. 使用两个参数`package`和`path`来初始化一个新的PathPatch实例。
2. `package`参数是可选的，可以为空或包含一个字符串值。
3. `path`参数是一个必需的字符串值，表示补丁的目标路径。
4. 创建并返回一个新的PathPatch实例，该实例包含了初始化的`package`和`path`字段。
### Vars
#### real_package_name
`real_package_name` 是一个变量，用于在给定包名和补丁包名之间进行匹配。如果存在补丁包名（即非空），则使用补丁包名；否则，使用原始包名。这个变量主要功能是提供一个统一的包名字符串，以确保在使用包时不会出现歧义或错误。
#### index_table
`index_table` 是一个变量，主要用于获取和操作一个 TOML 表。它在代码中被用来获取并修改一个包索引的表格配置。
#### patch_toml_table
`patch_toml_table` 是一个变量，主要功能是获取并操作一个名为 "patch" 的 TOML 表。这个表是通过调用 `toml_table.get_mut("patch").unwrap().as_table_mut().unwrap()` 语句获得的。它关联的主要函数是 `GetPackageIndexTable`，该函数用于进一步操作和获取与包索引相关的表。
#### mut file
`file` 是一个可变变量，关联的主要函数或类型是 `OpenOptions`。`OpenOptions` 是一个结构体，主要用于配置文件系统的打开选项。它包含以下字段：
- Create：一个布尔值，指示是否在文件不存在时创建新文件。
- Truncate：一个布尔值，指示是否在打开文件时截断文件到零长度。
- Mode：一个整数，用于设置文件的权限模式（Unix）或访问控制（Windows）。

`file` 变量的主要功能是打开一个文件以便追加内容。
#### mut patch_table
`patch_table`是一个可变变量，初始化为一个新的`Table`实例。它主要用于存储补丁信息或其他相关数据。
#### (mut toml_table, package_index)
let (mut toml_table, package_index) 是一个包含两个元素的元组，其中第一个元素是可变引用（mut）的 toml_table，第二个元素是 package_index。这个元组主要用于在 gen_patch_table 函数返回结果存在时，获取 patch 表的 mut 引用。

关联的主要函数是 `gen_patch_table` 和 `get_mut("patch")`，它们分别用于生成补丁表和获取 "patch" 表的可变引用。
## dependencies-patch::index_patch
 此包位于dependencies-patch::index_patch，专注于提供一个索引补丁的创建和管理工具。它包括一个主要功能是提供一个构造函数`new`，用于初始化IndexPatch实例。IndexPatch类型是一个结构体，包含两个字段：
- package: Option<String> - 包的真实名称可能在其Cargo.toml文件中被重命名。
- version: String - 补丁的版本号。
主要功能是提供一个构造函数`new`，用于初始化IndexPatch实例。此类型还与标准库中的字符串类型(String)和泛型枚举类型(Option)相关联。
### Functions
#### do_index_patch
do_index_patch函数的主要功能是将特定包的信息补丁到Git仓库中。

入参：
- cargo_path: 一个指向String类型的指针，表示Cargo项目的路径。
- package_name: 一个指向String类型的指针，表示要选择的包的名称。
- patch: 一个指向IndexPatch类型的指针，包含补丁信息。

主要执行流程：
1. 根据patch中的package字段或直接使用package_name来确定实际的包名（real_package_name）。
2. 调用gen_patch_table函数生成补丁表（toml_table）和包索引（package_index）。
3. 如果gen_patch_table返回的结果存在，则获取其补丁信息并插入到Cargo.toml文件中。
4. 打开Cargo.toml文件并在末尾追加补丁表的内容。
#### IndexPatch::new
IndexPatch类型用于创建一个新的索引补丁，包含包的真实名称和版本号。
IndexPatch结构体有两个字段：
- package: Option<String> - 包的真实名称可能在其Cargo.toml文件中被重命名。
- version: String - 补丁的版本号。
主要功能是提供一个构造函数`new`，用于初始化IndexPatch实例。
### Vars
#### (mut toml_table, package_index)
`toml_table` 是一个可变的全局变量，主要用于处理TOML格式的配置文件。它与函数 `gen_patch_table` 和 `SetBufferSizeLimit` 相关联。
#### mut file
`file` 是一个变量，主要功能是作为一个文件句柄，用于追加内容到指定的 Cargo.toml 文件中。关联的主要函数或类型是 `OpenOptions` 结构体，它用于配置文件系统的打开选项。具体字段包括：

- `Create`: 一个布尔值，指示是否在文件不存在时创建新文件。
- `Truncate`: 一个布尔值，指示是否在打开文件时截断文件到零长度。
- `Mode`: 一个整数，用于设置文件的权限模式（Unix）或访问控制（Windows）。
#### index_table
`index_table`是一个变量，用于获取并操作一个TOML表。它关联的主要函数或类型是`patch_toml_table`和`package_index`。
#### real_package_name
`real_package_name` 是一个变量，用于匹配并赋值包名。它在 `match` 语句中根据 `&patch.package` 的值来决定其具体值：

- 如果 `patch.package` 存在（即 `Some(name)`），则将其值赋给 `real_package_name`。
- 如果 `patch.package` 不存在（即 `None`），则使用预定义的 `package_name`。

该变量主要用于获取或设置包名，具体取决于 `patch.package` 是否存在。
#### patch_toml_table
`patch_toml_table` 是一个变量，主要用于获取并操作一个名为 "patch" 的 TOML 表。它关联的主要函数或类型是 Rust 语言中的 `get_mut`, `as_table_mut`, 和 `unwrap` 方法。
#### mut patch_table
`patch_table`是一个可变变量，初始化时为一个新的`Table`实例。这个变量主要用于存储补丁表信息，但没有关联的主要函数或类型。
## dependencies-patch::patch
 此包位于dependencies-patch::patch，主要功能不明确，可能是一个用于依赖关系管理的工具。目前没有公开的函数、类型或变量描述，因此无法提供具体的总结内容。建议提供更多的上下文信息以便更好地理解其用途和功能。
### Functions
#### gen_patch_table

gen_patch_table函数的主要功能是根据给定的Cargo项目路径、包名称和实际包名生成补丁表。它用于在Cargo.toml文件中插入或更新与指定包相关的补丁信息。
入参：
- cargo_path: 一个指向String类型的指针，表示Cargo项目的路径。
- package_name: 一个指向String类型的指针，表示要选择的包的名称。
- real_package_name: 一个指向String类型的指针，表示实际的包名。
出参：
- Some((patch_table, package_index)): 一个元组，包含补丁表和包索引。
主要执行流程：
1. 使用pick_package函数根据实际包名获取包信息。
2. 解析包依赖关系，判断是否存在补丁。
3. 如果补丁已存在或包是路径依赖，则返回None。
4. 初始化一个Cargo.toml表并插入补丁字段。
5. 根据包依赖类型设置补丁内容，返回补丁表和包索引。

#### patch
patch函数的主要功能是根据args参数中的patch_type字段，对指定的包路径进行补丁操作。具体来说，它会根据patch_type的不同值，执行不同的补丁操作：

- 如果patch_type为"git"，则它会创建一个GitPatch实例，并调用do_git_patch函数进行处理。
- 如果patch_type为"registry"，则它会创建一个IndexPatch实例，并调用do_index_patch函数进行处理。
- 对于其他情况（即patch_type不匹配上述两种情况），则会创建一个PathPatch实例，并调用do_path_patch函数进行处理。

具体执行流程如下：
1. 从args参数中提取cargo_path字段，该字段表示Cargo项目的路径。
2. 根据patch_type的值，执行相应的补丁操作：
   - 如果patch_type为"git"，则进一步检查commit、tag和branch字段的值（如果有），并创建一个GitInfo实例来存储这些信息。然后使用这些信息和args中的其他参数来创建一个GitPatch实例，最后调用do_git_patch函数进行处理。
   - 如果patch_type为"registry"，则直接使用args中的参数来创建一个IndexPatch实例，并调用do_index_patch函数进行处理。
   - 对于其他情况，则根据args中的参数创建一个PathPatch实例，并调用do_path_patch函数进行处理。
3. 根据不同的补丁类型执行相应的补丁操作。
#### check_patch_exist
Check whether the patch exists for the specific package
入参：
- cargo_path: &String - 包含项目路径的字符串引用
- package_name: &String - 包名称的字符串引用
- package_dependency: &Dependency - 依赖类型的引用
出参：
- bool - 布尔值，表示补丁是否存在

主要执行流程：
1. 构建Cargo.toml文件路径。
2. 读取并解析Cargo.toml文件内容。
3. 检查补丁表是否包含指定包的名称或Git地址。
4. 根据依赖类型进一步检查补丁表中是否存在相关补丁。
### Vars
#### cargo_toml_path
`cargo_toml_path`是一个字符串变量，用于表示Cargo.toml文件的路径。它通过将`cargo_path`和字符串`"/Cargo.toml"`拼接而成。
#### patch_table
`patch_table`是一个变量，用于获取并操作Cargo.toml文件中的“patch”部分。它是一个表（table），允许对其进行修改。
#### git_patch
`git_patch` 是一个结构体变量，主要功能是存储 Git 仓库的相关信息。它包含以下字段：
- git: String, 表示 Git 仓库名称。
- package: Option<String>, 可能包含包的重命名信息。
- version: Option<String>, 补丁版本信息。
- info: GitInfo, 补丁目标信息。

关联的主要类型是 `GitInfo`，这是一个枚举类型，用于表示 Git 仓库的信息，包含以下几种变体：
- None: 没有特定的信息。
- Commit(String): 提交哈希值，表示一个具体的提交。
- Tag(String): 标签名称，表示一个具体的标签。
- Branch(String): 分支名称，表示一个具体的分支。

此外，还涉及到的类型包括 `String` 和 `Option`，其中 `String` 用于表示文本数据，而 `Option` 是一个枚举类型，用于表示可能存在的值或可能缺失的值。
#### path_patch
`path_patch` 是一个变量，属于 `PathPatch` 类型的实例。这个类型是一个结构体，用于表示对包路径的补丁信息。它包含两个字段：
   - `package`: 一个可选的字符串类型，表示可能在 Cargo.toml 文件中被重命名的实际包名。
   - `path`: 一个字符串类型，表示补丁的目标路径。

主要功能和用途是提供对包路径的详细描述，以便在构建系统或版本控制系统中进行管理和调整。
#### registry_table
`registry_table`是一个变量，用于获取一个名为 "crates-io" 的表（可能是从某个配置或数据结构中）。这个表是从 `patch_table` 中获取的，确保了这个操作不会失败（通过 `unwrap()` 方法）。
#### mut git_info
`git_info` 是一个可变的变量，初始值为 `GitInfo::None`。它是一个枚举类型，用于表示 Git 仓库的信息。主要包含以下几种变体：
- `None`: 没有特定的信息。
- `Commit(String)`: 提交哈希值，表示一个具体的提交。
- `Tag(String)`: 标签名称，表示一个具体的标签。
- `Branch(String)`: 分支名称，表示一个具体的分支。

该类型主要用于在 Rust 代码中表示 Git 仓库的不同信息状态，以便进行版本控制和标识。
#### cargo_toml
cargo_toml是一个表变量，用于解析和存储Cargo.toml文件的内容。它通过调用toml::from_str函数从字符串中解析Cargo.toml文件内容并赋值给cargo_toml变量。
#### cargo_path
`cargo_path`是一个变量，它从命令行参数中获取路径并解包。主要功能是提供一个文件或目录的路径，供后续程序使用。
#### index_patch
`index_patch`是一个`IndexPatch`类型的变量，主要功能是存储包的真实名称和版本号。它包含两个字段：`package`和`version`。

- `package`是一个可选的字符串类型（`Option<String>`），表示包的实际名称，可能在其Cargo.toml文件中被重命名。
- `version`是一个标准库中的字符串类型，表示补丁的版本号。
#### mut cargo_toml
cargo_toml 是一个可变的全局变量，类型为 Table。它主要用于管理 Cargo.toml 文件的配置信息。与它相关的函数或方法包括获取和修改配置项。
#### package
let package是一个变量，用于在匹配pick_package函数的返回结果时存储包信息。如果pick_package函数调用成功（即返回Ok），则将返回的包赋值给package；如果失败（返回Err），则会记录错误日志并返回None。
#### package_dependency
`package_dependency`是一个变量，它通过调用`package.parse_dependency()`方法来解析包依赖。主要功能是存储解析后的包依赖信息，没有关联的主要函数或类型。
## dependencies-patch
 该包位于dependencies-patch，主要功能不明确，没有公开的函数、类型或变量描述。
### Functions
#### main
main函数的主要功能是解析命令行参数并将这些参数传递给patch函数进行进一步处理。如果解析命令行参数成功，则继续调用patch函数对指定的包路径进行补丁操作；否则，直接返回。

入参：
- 无
出参：
- 无

主要执行流程如下：
1. 使用`parse_args`函数解析命令行参数，并将其存储在变量`args`中。如果解析失败，则程序直接返回。
2. 调用`patch`函数，根据`args`中的`patch_type`字段，对指定的包路径进行相应的补丁操作：
   - 如果`patch_type`为"git"，则创建一个GitPatch实例并调用do_git_patch函数进行处理。
   - 如果`patch_type`为"registry"，则创建一个IndexPatch实例并调用do_index_patch函数进行处理。
   - 对于其他情况（即`patch_type`不匹配上述两种情况），则创建一个PathPatch实例并调用do_path_patch函数进行处理。
### Vars
#### args
`args`是一个变量，用于存储解析命令行参数的结果。如果没有通过`parse_args()`函数成功解析到参数，程序将直接退出（return）。

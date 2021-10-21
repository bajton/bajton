# coding=utf-8
from __future__ import unicode_literals

default_env = ["LANG=en_US.UTF-8", "LANGUAGE=en_US:en", "LC_ALL=en_US.UTF-8"]


c_lang_config = {
    "compile": {
        "src_name": "main.c",
        "exe_name": "main",
        "max_cpu_time": 3000,
        "max_real_time": 5000,
        "max_memory": 128 * 1024 * 1024,
        "compile_command": "/usr/bin/gcc -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c99 {src_path} -lm -o {exe_path}",
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": "c_cpp",
        "env": default_env
    }
}

c_lang_spj_compile = {
    "src_name": "spj-{spj_version}.c",
    "exe_name": "spj-{spj_version}",
    "max_cpu_time": 3000,
    "max_real_time": 5000,
    "max_memory": 1024 * 1024 * 1024,
    "compile_command": "/usr/bin/gcc -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c99 {src_path} -lm -o {exe_path}"
}

c_lang_spj_config = {
    "exe_name": "spj-{spj_version}",
    "command": "{exe_path} {in_file_path} {user_out_file_path}",
    "seccomp_rule": "c_cpp"
}

cpp_lang_config = {
    "compile": {
        "src_name": "main.cpp",
        "exe_name": "main",
        "max_cpu_time": 3000,
        "max_real_time": 5000,
        "max_memory": 128 * 1024 * 1024,
        "compile_command": "/usr/bin/g++ -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c++11 {src_path} -lm -o {exe_path}",
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": "c_cpp",
        "env": default_env
    }
}

rust_lang_config = {
    "compile": {
        "src_name": "raw.rs",
        "exe_name": "main",
        "max_cpu_time": 3000,
        "max_real_time": 5000,
        "max_memory": 128 * 1024 * 1024,
        # "compile_command": """/bin/bash -c "/usr/bin/cargo -q new ru && cp {src_path} ./ru/src/main.rs && cd ./ru && cargo -q build --offline --release && cp ./target/release/ru {exe_path} && cd .." """,
        "compile_command": """/usr/bin/rustc {src_path} -L /usr/lib -o {exe_path}""",
        "env": ["RUSTUP_HOME=/rust", "CARGO_HOME=/rust"] + default_env
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": None,
        "env": default_env
    }
}

java_lang_config = {
    "name": "java",
    "compile": {
        "src_name": "Main.java",
        "exe_name": "Main",
        "max_cpu_time": 3000,
        "max_real_time": 5000,
        "max_memory": -1,
        "compile_command": "/usr/bin/javac {src_path} -d {exe_dir} -encoding UTF8"
    },
    "run": {
        "command": "/usr/bin/java -cp {exe_dir} -XX:MaxRAM={max_memory}k -Dfile.encoding=UTF-8 -Djava.security.policy==/etc/java_policy -Djava.awt.headless=true Main",
        "seccomp_rule": None,
        "env": default_env,
        "memory_limit_check_only": 1
    }
}

csharp_lang_config = {
    "name": "csharp",
    "compile": {
        "src_name": "Main.cs",
        "exe_name": "Main.exe",
        "max_cpu_time": 3000,
        "max_real_time": 5000,
        "max_memory": -1,
        "compile_command": "/usr/bin/mcs {src_path} -out:{exe_path}"
    },
    "run": {
        "command": "/usr/bin/mono {exe_path}",
        "seccomp_rule": None,
        "env": default_env,
        "memory_limit_check_only": 1
    }
}

py3_lang_config = {
    "compile": {
        "src_name": "solution.py",
        "exe_name": "__pycache__/solution.cpython-310.pyc",
        "max_cpu_time": 3000,
        "max_real_time": 5000,
        "max_memory": 128 * 1024 * 1024,
        "compile_command": "/usr/bin/python3.10 -m py_compile {src_path}",
    },
    "run": {
        "command": "/usr/bin/python3 {exe_path}",
        "seccomp_rule": "general",
        "env": ["PYTHONIOENCODING=UTF-8"] + default_env
    }
}

go_lang_config = {
    "compile": {
        "src_name": "main.go",
        "exe_name": "main",
        "max_cpu_time": 3000,
        "max_real_time": 5000,
        "max_memory": 1024 * 1024 * 1024,
        "compile_command": "/usr/bin/go build -o {exe_path} {src_path}",
        "env": ["GOCACHE=/tmp", "GOPATH=/tmp/go"]
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": "",
        # 降低内存占用
        "env": ["GODEBUG=madvdontneed=1", "GOCACHE=off"] + default_env,
        "memory_limit_check_only": 1
    }
}

php_lang_config = {
    "run": {
        "exe_name": "solution.php",
        "command": "/usr/bin/php {exe_path}",
        "seccomp_rule": "",
        "env": default_env,
        "memory_limit_check_only": 1
    }
}

perl_lang_config = {
    "compile": {
        "src_name": "main.pl",
        "exe_name": "main.pl",
        "max_cpu_time": 3000,
        "max_real_time": 5000,
        "max_memory": 1024 * 1024 * 1024,
        "compile_command": "/usr/bin/perl -c {src_path}",
        "env": []
    },
    "run": {
        "exe_name": "main.pl",
        "command": "/usr/bin/perl {exe_path}",
        "seccomp_rule": "",
        "env": [],
        "memory_limit_check_only": 1
    }
}

js_lang_config = {
    "run": {
        "exe_name": "solution.js",
        "command": "/usr/bin/node {exe_path}",
        "seccomp_rule": "",
        "env": ["NO_COLOR=true"] + default_env,
        "memory_limit_check_only": 1
    }
}

ts_lang_config = {
    "run": {
        "exe_name": "solution.ts",
        "command": "/usr/bin/ts-node {exe_path}",
        "seccomp_rule": "",
        "env": default_env,
        "memory_limit_check_only": 1
    }
}
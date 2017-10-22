// RUN: %swiftc_driver -driver-print-jobs -target x86_64-apple-macosx10.9  -g -sdk %S/../Inputs/clang-importer-sdk %s 2>&1 | %FileCheck %s --check-prefix OSX
// RUN: %swiftc_driver -driver-print-jobs -target x86_64-unknown-linux-gnu -g -sdk %S/../Inputs/clang-importer-sdk %s 2>&1 | %FileCheck %s --check-prefix LINUX 
// RUN: %swiftc_driver -driver-print-jobs -target x86_64-unknown-freebsd   -g -sdk %S/../Inputs/clang-importer-sdk %s 2>&1 | %FileCheck %s --check-prefix FREEBSD

// RUN: env SDKROOT=%S/../Inputs/clang-importer-sdk %swiftc_driver_plain -target x86_64-apple-macosx10.9  -g -driver-print-jobs %s 2>&1 | %FileCheck %s --check-prefix OSX
// RUN: env SDKROOT=%S/../Inputs/clang-importer-sdk %swiftc_driver_plain -target x86_64-unknown-linux-gnu -g -driver-print-jobs %s 2>&1 | %FileCheck %s --check-prefix LINUX
// RUN: env SDKROOT=%S/../Inputs/clang-importer-sdk %swiftc_driver_plain -target x86_64-unknown-freebsd   -g -driver-print-jobs %s 2>&1 | %FileCheck %s --check-prefix FREEBSD

// OSX-NOT: warning: no such SDK:
// OSX: bin/swift
// OSX-SAME: Driver/sdk.swift
// OSX-SAME: -sdk {{.*}}/Inputs/clang-importer-sdk
// OSX-NEXT: bin/{{.+}} {{.*}}.o{{[ "]}}
// OSX-SAME: {{-syslibroot|--sysroot}} {{.*}}/Inputs/clang-importer-sdk

// LINUX-NOT: warning: no such SDK:
// LINUX: bin/swift
// LINUX-SAME: Driver/sdk.swift
// LINUX-SAME: -sdk {{.*}}/Inputs/clang-importer-sdk
// LINUX: bin/{{.+}} {{.*}}swift_begin.o
// LINUX-SAME: {{-syslibroot|--sysroot}} {{.*}}/Inputs/clang-importer-sdk
// LINUX-SAME: {{.*}}swift_end.o

// FREEBSD-NOT: warning: no such SDK:
// FREEBSD: bin/swift
// FREEBSD-SAME: Driver/sdk.swift
// FREEBSD-SAME: -sdk {{.*}}/Inputs/clang-importer-sdk
// FREEBSD: bin/{{.+}} {{.*}}swift_begin.o
// FREEBSD-SAME: {{-syslibroot|--sysroot}} {{.*}}/Inputs/clang-importer-sdk
// FREEBSD-SAME: {{.*}}swift_end.o

// RUN: %swift_driver -driver-print-jobs -repl -sdk %S/Inputs/nonexistent-sdk 2>&1 | %FileCheck %s --check-prefix=SDKWARNING
// RUN: %swift_driver -driver-print-jobs -sdk %S/Inputs/nonexistent-sdk 2>&1 | %FileCheck %s --check-prefix=SDKWARNING
// RUN: env SDKROOT=%S/Inputs/nonexistent-sdk %swift_driver_plain -driver-print-jobs -repl 2>&1 | %FileCheck %s --check-prefix=SDKWARNING

// SDKWARNING: warning: no such SDK: '{{.*}}/Inputs/nonexistent-sdk'
// SDKWARNING: -sdk {{.*}}/Inputs/nonexistent-sdk

// RUN: %swiftc_driver -driver-print-jobs -typecheck -sdk %S/../Inputs/clang-importer-sdk -module-cache-path /path/to/cache %s 2>&1 | %FileCheck %s --check-prefix=CACHE-PATH

// CACHE-PATH: -module-cache-path /path/to/cache

# FIXME: ICU is only needed on a per-target basis, for targets that are not
#        Darwin. For example:
#
#        - When the host is macOS, and the target is Android, ICU is needed.
#        - When the host is macOS, and the target is iOS, ICU is not needed.
#
#        Currently, no matter this target, this checks the host.
if(NOT SWIFT_HOST_VARIANT MATCHES "${SWIFT_DARWIN_VARIANTS}")
  find_package(ICU REQUIRED COMPONENTS uc i18n)
endif()

set(swift_stubs_sources
    Assert.cpp
    CommandLine.cpp
    GlobalObjects.cpp
    LibcShims.cpp
    Stubs.cpp
    UnicodeExtendedGraphemeClusters.cpp.gyb)
set(swift_stubs_objc_sources
    Availability.mm
    DispatchShims.mm
    FoundationHelpers.mm
    Reflection.mm
    SwiftNativeNSXXXBase.mm.gyb)
set(swift_stubs_unicode_normalization_sources
    UnicodeNormalization.cpp)
set(LLVM_OPTIONAL_SOURCES
    ${swift_stubs_objc_sources}
    ${swift_stubs_unicode_normalization_sources})

set(swift_stubs_c_compile_flags
    ${SWIFT_RUNTIME_CORE_CXX_FLAGS} -DswiftCore_EXPORTS)

add_swift_library(swiftStdlibStubs OBJECT_LIBRARY TARGET_LIBRARY
  ${swift_stubs_sources}
  ${swift_stubs_objc_sources}
  C_COMPILE_FLAGS ${swift_stubs_c_compile_flags}
  LINK_FLAGS ${SWIFT_RUNTIME_CORE_LINK_FLAGS}
  LINK_LIBRARIES ${swift_stubs_link_libraries}
  TARGET_SDKS ALL_APPLE_PLATFORMS
  INSTALL_IN_COMPONENT stdlib)

add_swift_library(swiftStdlibStubs OBJECT_LIBRARY TARGET_LIBRARY
  ${swift_stubs_sources}
  ${swift_stubs_unicode_normalization_sources}
  C_COMPILE_FLAGS ${swift_stubs_c_compile_flags}
  LINK_FLAGS ${SWIFT_RUNTIME_CORE_LINK_FLAGS}
  LINK_LIBRARIES ${swift_stubs_link_libraries}
  TARGET_SDKS ANDROID CYGWIN FREEBSD LINUX
  INSTALL_IN_COMPONENT stdlib)


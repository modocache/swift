# libswiftRemoteMirror.dylib should not have runtime dependencies; it's
# always built as a shared library.
message(STATUS ">>> SWIFT_RUNTIME_CXX_FLAGS: ${SWIFT_RUNTIME_CXX_FLAGS}")
message(STATUS ">>> SWIFT_RUNTIME_LINK_FLAGS: ${SWIFT_RUNTIME_LINK_FLAGS}")
if(SWIFT_BUILD_DYNAMIC_STDLIB OR SWIFT_BUILD_REMOTE_MIRROR)
  add_swift_library(swiftRemoteMirror SHARED TARGET_LIBRARY DONT_EMBED_BITCODE
      SwiftRemoteMirror.cpp
      LINK_LIBRARIES swiftReflection
      C_COMPILE_FLAGS ${SWIFT_RUNTIME_CXX_FLAGS}
      LINK_FLAGS ${SWIFT_RUNTIME_LINK_FLAGS}
      TARGET_SDKS "${SWIFT_HOST_VARIANT_SDK}"
      INSTALL_IN_COMPONENT swift-remote-mirror)
endif()

set(SourceKitSupport_sources
  FuzzyStringMatcher.cpp
  Logging.cpp
  ImmutableTextBuffer.cpp
  ThreadSafeRefCntPtr.cpp
  Tracing.cpp
  UIDRegistry.cpp
)

set(SourceKitSupport_InProc_sources Concurrency-InProc.cpp)
set(SourceKitSupport_XPC_sources Concurrency-Mac.cpp)

set(LLVM_OPTIONAL_SOURCES ${SourceKitSupport_InProc_sources})
set(LLVM_OPTIONAL_SOURCES ${SourceKitSupport_XPC_sources})

if(SWIFT_SOURCEKIT_USE_INPROC_LIBRARY)
  list(APPEND SourceKitSupport_sources ${SourceKitSupport_InProc_sources})
else()
  list(APPEND SourceKitSupport_sources ${SourceKitSupport_XPC_sources})
endif()

add_sourcekit_library(SourceKitSupport
  ${SourceKitSupport_sources}
  DEPENDS swiftBasic clangBasic clangRewrite
)

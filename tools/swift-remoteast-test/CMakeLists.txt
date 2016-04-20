add_swift_target_executable(swift-remoteast-test
  swift-remoteast-test.cpp
  LINK_LIBRARIES
    swiftRemoteAST
  # swiftRemoteAST and its dependencies must be linked against uuid,
  # rt, tinfo, and pthread--none of which are available on Android.
  EXCLUDE_SDKS
    ANDROID)
// RUN: %target-run-stdlib-swift
// REQUIRES: executable_test

// REQUIRES: objc_interop

// watchOS 2.0 does not have a public XCTest module.
// XFAIL: OS=watchos

import StdlibUnittest
import XCTest

var XCTestTestSuite = TestSuite("XCTest")

XCTestTestSuite.test("XCTAssertTrue") {
  class MyTestCase: XCTestCase {
    func test_myThing() {
      XCTAssertEqual(1, 2)
    }
  }

  let testCase = MyTestCase(selector: "test_myThing")
  testCase.runTest()
  let run = testCase.testRun!

  expectEqual(1, run.testCaseCount)
  expectEqual(1, run.executionCount)
  expectEqual(1, run.failureCount)
  expectEqual(0, run.unexpectedExceptionCount)
  expectEqual(1, run.totalFailureCount)
  expectFalse(run.hasSucceeded)
}

runAllTests()


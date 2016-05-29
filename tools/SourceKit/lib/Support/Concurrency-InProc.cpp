//===--- Concurrency-InProc.cpp -------------------------------------------===//
//
// This source file is part of the Swift.org open source project
//
// Copyright (c) 2014 - 2016 Apple Inc. and the Swift project authors
// Licensed under Apache License v2.0 with Runtime Library Exception
//
// See http://swift.org/LICENSE.txt for license information
// See http://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
//
//===----------------------------------------------------------------------===//

#include "SourceKit/Support/Concurrency.h"
#include "SourceKit/Config/config.h"
#include "llvm/Support/ErrorHandling.h"

using namespace SourceKit;

void *WorkQueue::Impl::create(Dequeuing DeqKind, Priority Prio,
                              llvm::StringRef Label) {
 llvm::report_fatal_error("not yet implemented");
}

void WorkQueue::Impl::dispatch(Ty Obj, const DispatchData &Fn) {
  llvm::report_fatal_error("not yet implemented");
}

void WorkQueue::Impl::dispatchSync(Ty Obj, const DispatchData &Fn) {
  llvm::report_fatal_error("not yet implemented");
}

void WorkQueue::Impl::dispatchBarrierSync(Ty Obj, const DispatchData &Fn) {
  llvm::report_fatal_error("not yet implemented");
}

void WorkQueue::Impl::dispatchOnMain(const DispatchData &Fn) {
  llvm::report_fatal_error("not yet implemented");
}

void WorkQueue::Impl::dispatchConcurrent(Priority Prio, const DispatchData &Fn) {
  llvm::report_fatal_error("not yet implemented");
}

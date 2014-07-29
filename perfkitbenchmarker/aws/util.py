#!/usr/bin/env python
# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Utilities for working with Amazon Web Services resources."""

import gflags as flags

from perfkitbenchmarker import perfkitbenchmarker_lib

AWS_PATH = 'aws'
FLAGS = flags.FLAGS


def AddDefaultTags(resource_id, region):
  """Adds tags to an AWS resource created by PerfKitBenchmarker.

  By default, resources are tagged with "owner" and "perfkitbenchmarker-run"
  key-value
  pairs.

  Args:
    resource_id: An extant AWS resource to operate on.
    region: The AWS region 'resource_id' was created in.
  """
  tag_cmd = [AWS_PATH,
             'ec2',
             'create-tags',
             '--region=%s' % region,
             '--resources', resource_id,
             '--tags',
             'Key=owner,Value="{0}"'.format(FLAGS.owner),
             'Key=perfkitbenchmarker-run,Value="{0}"'.format(FLAGS.run_uri)]
  perfkitbenchmarker_lib.IssueRetryableCommand(tag_cmd)

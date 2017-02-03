# Copyright 2017 PerfKitBenchmarker Authors. All rights reserved.
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


"""Module containing SHOC Benchmark Suite installation and
   cleanup functions.
"""

import re

from perfkitbenchmarker.linux_packages import INSTALL_DIR
from perfkitbenchmarker import data
import os

SHOC_GIT_URL = 'https://github.com/vetter/shoc.git'
SHOC_DIR = '%s/shoc' % INSTALL_DIR
SHOC_BIN_DIR = os.path.join(SHOC_DIR, 'bin')
SHOC_PATCH = 'shoc_config.patch'
APT_PACKAGES = 'wget automake git zip'

def AptInstall(vm):
  """Installs the CUDA HPL package on the VM."""
  vm.InstallPackages(APT_PACKAGES)
  vm.Install('cuda_toolkit_8')
  vm.RemoteCommand('export PATH=$PATH:/usr/local/cuda/bin') #TODO: Ugly!
  vm.RemoteCommand('git clone %s' % SHOC_GIT_URL)
  vm.RemoteCommand('cd %s && ./configure' % SHOC_DIR)
  vm.PushFile(data.ResourcePath(SHOC_PATCH), INSTALL_DIR)
  vm.RemoteCommand('cd %s && patch -p0 < %s' % (INSTALL_DIR, SHOC_PATCH))
  vm.RemoteCommand('cd %s && make -j8' % (SHOC_DIR, SHOC_DIR))


def YumInstall(vm):
  """TODO: PKB currently only supports the installation of SHOC
     on Ubuntu.
  """
  raise NotImplementedError()

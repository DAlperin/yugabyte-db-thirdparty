#
# Copyright (c) YugaByte, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations
# under the License.
#

from yugabyte_db_thirdparty.build_definition_helpers import *  # noqa


class LibBacktraceDependency(Dependency):
    def __init__(self) -> None:
        super(LibBacktraceDependency, self).__init__(
            name='libbacktrace',
            version='ba79a27ee9a62b1be86d0ddae7614c316b7f6fbb',
            url_pattern='https://github.com/yugabyte/libbacktrace/archive/{0}.zip',
            build_group=BUILD_GROUP_INSTRUMENTED)
        self.copy_sources = True

    def build(self, builder: BuilderInterface) -> None:
        builder.build_with_configure(dep=self, extra_args=['--with-pic'])

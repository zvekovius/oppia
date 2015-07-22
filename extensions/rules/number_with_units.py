# coding: utf-8
#
# Copyright 2014 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, softwar
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Rules for NumberWithUnits."""

__author__ = 'Sean Lip'

from extensions.rules import base


class Equals(base.NumberWithUnitsRule):
    description = 'is equal to {{x|Real}} {{y|UnicodeString}}'
    is_generic = False

    def _evaluate(self, subject):
        return subject['number'] == self.x and subject['units'] == self.y
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from smaug import exception
from smaug.i18n import _
from smaug.services.operationengine.operations import base


class ProtectOperation(base.Operation):
    """Protect operation."""

    OPERATION_TYPE = "protect"

    @classmethod
    def check_operation_definition(cls, operation_definition):
        if "plan_id" not in operation_definition:
            reason = _("Plan_id is not exist")
            raise exception.InvalidOperationDefinition(reason=reason)

    @classmethod
    def _execute(cls, operation_definition, param):
        # plan_id = operation_definition.get("plan_id")
        # TODO(chenzeng): invoke create checkpoint interface
        pass

    @classmethod
    def _resume(cls, operation_definition, param, log_ref):
        # plan_id = operation_definition.get("plan_id")
        # TODO(chenzeng): invoke create checkpoint interface
        pass

# TheBlackmad
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from ShellyPool import ShellyAppliance
from ShellyPool import ShellyPlugS
from ShellyPool import ShellyHTSensor
from ShellyPool import ShellyButton

NAME = "ShellyPool"
VERSION = "0.1.1"

TIMEOUT_DISCOVERY = 10

SHELLY_TYPE_CLASS = {
	'SHPLG-S': ShellyPlugS,
	'SHHT-1': ShellyHTSensor,
	'SHBTN-2': ShellyButton	
}

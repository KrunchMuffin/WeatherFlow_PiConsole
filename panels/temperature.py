""" Defines the Temperature panel required by the Raspberry Pi Python console
for WeatherFlow Tempest and Smart Home Weather stations.
Copyright (C) 2018-2023 Peter Davis

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

# Load required Kivy modules
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties         import StringProperty

# Load required panel modules
from panels.template         import panelTemplate


# ==============================================================================
# TemperaturePanel AND TemperatureButton CLASS
# ==============================================================================
class TemperaturePanel(panelTemplate):

    # Define TemperaturePanel class properties
    feelsLikeIcon = StringProperty('-')

    # Initialise TemperaturePanel
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setFeelsLikeIcon()

    # Set "Feels Like" icon
    def setFeelsLikeIcon(self):
        self.feelsLikeIcon = self.app.CurrentConditions.Obs['FeelsLike'][3]


class TemperatureButton(RelativeLayout):
    pass

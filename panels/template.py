""" Define the panel template for the Raspberry Pi Python console for
WeatherFlow Tempest and Smart Home Weather stations.
Copyright (C) 2018-2021 Peter Davis

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

# Load required modules
from kivy.uix.relativelayout import RelativeLayout
from kivy.app                import App


# ==============================================================================
# panelTemplate CLASS
# ==============================================================================
class panelTemplate(RelativeLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not hasattr(App.get_running_app(), self.__class__.__name__):
            panelList = []
        else:
            panelList = getattr(App.get_running_app(), self.__class__.__name__, 'panelList')
        panelList.append(self)
        setattr(App.get_running_app(), self.__class__.__name__, panelList)
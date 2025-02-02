# Copyright © 2017-2018 Joseph Lorimer <joseph@lorimer.me>
#
# This file is part of Chinese Support 3.
#
# Chinese Support 3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# Chinese Support 3 is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# Chinese Support 3.  If not, see <https://www.gnu.org/licenses/>.

from anki.hooks import addHook, wrap
from anki.lang import _
from anki.stats import CollectionStats
from anki.stdmodels import models
from aqt import mw

from .config import ConfigManager
from .database import Dictionary

config = ConfigManager()
dictionary = Dictionary()

from .edit import append_tone_styling, EditManager
from .graph import todayStats
from .gui import load_menu, unload_menu
from .models import advanced, basic
from .templates import chinese, ruby


if config['firstRun']:
    dictionary.create_indices()
    config['firstRun'] = False


def load():
    ruby.install()
    chinese.install()
    addHook('profileLoaded', load_menu)
    addHook('profileLoaded', add_models)
    addHook('loadNote', append_tone_styling)
    addHook('unloadProfile', config.save)
    addHook('unloadProfile', dictionary.conn.close)
    addHook('unloadProfile', unload_menu)
    CollectionStats.todayStats = wrap(
        CollectionStats.todayStats, todayStats, 'around'
    )
    EditManager()


def add_models():
    models.append(('Chinese (Advanced)', advanced.add_model))
    models.append(('Chinese (Basic)', basic.add_model))
    # if not mw.col.models.by_name('Chinese (Advanced)'):
    #     advanced.add_model(mw.col)
    # if not mw.col.models.by_name('Chinese (Basic)'):
    #     basic.add_model(mw.col)

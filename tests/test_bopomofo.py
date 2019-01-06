# Copyright © 2018-2019 Joseph Lorimer <luoliyan@posteo.net>
#
# This file is part of Chinese Support Redux.
#
# Chinese Support Redux is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# Chinese Support Redux is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# Chinese Support Redux.  If not, see <https://www.gnu.org/licenses/>.

from unittest import skip

from chinese.bopomofo import bopomofo
from tests import ChineseTest


class Bopomofo(ChineseTest):
    def test_pinyin_no_tone(self):
        self.assertEqual(bopomofo(['zhu yin']), ['ㄓㄨ ㄧㄣ'])
        self.assertEqual(bopomofo(['zhu', 'yin']), ['ㄓㄨ', 'ㄧㄣ'])
        self.assertEqual(bopomofo(['zhuyin']), ['ㄓㄨㄧㄣ'])

    def test_pinyin_tone_numbers(self):
        self.assertEqual(
            bopomofo(['ni3', 'ne5', 'ru2guo3 zhu4 yin1']),
            ['ㄋㄧˇ', 'ㄋㄜ˙', 'ㄖㄨˊㄍㄨㄛˇ ㄓㄨˋ ㄧㄣ'],
        )

        self.assertEqual(bopomofo(['mei2 you3']), ['ㄇㄟˊ ㄧㄡˇ'])

    @skip
    def test_pinyin_tone_mark(self):
        self.assertEqual(bopomofo('zhù yīn'), '')

    @skip
    def test_joined_word(self):
        self.assertEqual(bopomofo('zhùyīn'), '')

    @skip
    def test_hanzi(self):
        self.assertEqual(bopomofo('注音'), '')

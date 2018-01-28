# -*- coding: utf-8 -*-


class HistoryFactory:
    def creatHistory(self, month):
        try:
            exec ('from historydata import history{m}'.format(m=month))
            exec ('h = history{m}.History{m}()'.format(m=month))
            print('historyfactory未出错')
            return h
        except:
            print('historyfactory粗错，选择了random')
            from historydata import historyRandom
            return historyRandom.HistoryRandom()

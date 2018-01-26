# -*- coding: utf-8 -*-


class HistoryFactory:
    def creatHistory(self, month):
        try:
            print('未出错')
            exec ('from historydata import history{m}'.format(m=month))
            exec ('h = history{m}.History{m}()'.format(m=month))
            return h
        except:
            print('出错了')
            from historydata import historyRandom
            return historyRandom.HistoryRandom()

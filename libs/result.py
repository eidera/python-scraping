# -*- coding: utf-8 -*-

from libs.store import Store

class Result:
    PRIMARY_KEY = 'url'
    PERMIT_COLUMNS = ['url', 'html', 'scraped_at']

    def __init__(self):
        self.store = Store()

    def save(self, seeds):
        prepared = self._prepare(seeds)
        record = self._get_record(seeds['url'])
        if record is not None:
            self._update(record, prepared)
            return

        self._insert(prepared)

    def _prepare(self, seeds):
        results = {}
        for column in self.PERMIT_COLUMNS:
            value = seeds.get(column)
            if value is not None:
                results[column] = value
        return results

    def _get_db(self):
        return self.store.get_db()

    def _get_record(self, primary_key):
        conditions = {}
        conditions[self.PRIMARY_KEY] = primary_key
        db = self._get_db()
        return db.results.filter_by(**conditions).first()

    def _insert(self, seeds):
        db = self._get_db()
        db.results.insert(**seeds)
        db.commit()

    def _update(self, profile, seeds):
        for k, v in seeds.items():
            setattr(profile, k, v)

        db = self._get_db()
        db.commit()

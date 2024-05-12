import time
from contextlib import contextmanager
from typing import Dict


class Timer:
    def __init__(self):
        self.entries: Dict[str, float] = {}

    @contextmanager
    def track(self, entry_name: str):
        start_time = time.time()
        yield
        end_time = time.time()
        self._add_entry(entry_name, end_time - start_time)

    def _add_entry(self, entry_name: str, entry_val: float):
        self.entries[entry_name] = entry_val

    def dump_stats(self) -> str:
        result = "=====TIMER_STATS_START=====\n"
        for entry_name, entry_seconds in self.entries.items():
            result += f"{entry_name}: {entry_seconds:.2f} s || {entry_seconds/60:.2f} mins\n"
        result += "=====TIEMR_STATS_END======="
        return result
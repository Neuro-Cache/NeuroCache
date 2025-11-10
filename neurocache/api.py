"""
Public API that uses the private core if installed; otherwise a safe demo fallback.
"""
try:
    from neurocache_core import NeuroCore  # private, commercial-only package
    _HAS_CORE = True
except Exception:
    _HAS_CORE = False

class _DemoSTS:
    def __init__(self, capacity: int = 256):
        self.capacity = int(capacity)
        self._store = {}

    def get(self, key):
        return self._store.get(key)

    def put(self, key, value):
        if len(self._store) >= self.capacity:
            self._store.pop(next(iter(self._store)))  # naive FIFO for demo
        self._store[key] = value

class NeuroCacheAPI:
    def __init__(self, *args, **kwargs):
        self.impl = NeuroCore(*args, **kwargs) if _HAS_CORE else _DemoSTS(*args, **kwargs)

    def get(self, key): return self.impl.get(key)
    def put(self, key, value): return self.impl.put(key, value)

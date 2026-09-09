class HybridLogicalClock:
    """Hybrid Logical Clock (HLC) ensuring causal consistency with bounded drift."""
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.l = 0 # physical time component
        self.c = 0 # logical counter component

    def now(self, physical_time: int) -> dict:
        l_prime = self.l
        self.l = max(l_prime, physical_time)
        if self.l == l_prime:
            self.c += 1
        else:
            self.c = 0
        return {"l": self.l, "c": self.c, "node": self.node_id, "timestamp": f"{self.l}:{self.c}"}

    def update(self, msg_l: int, msg_c: int, physical_time: int) -> dict:
        l_prime = self.l
        self.l = max(l_prime, physical_time, msg_l)
        if self.l == l_prime and self.l == msg_l:
            self.c = max(self.c, msg_c) + 1
        elif self.l == l_prime:
            self.c += 1
        elif self.l == msg_l:
            self.c = msg_c + 1
        else:
            self.c = 0
        return {"l": self.l, "c": self.c, "node": self.node_id, "timestamp": f"{self.l}:{self.c}"}

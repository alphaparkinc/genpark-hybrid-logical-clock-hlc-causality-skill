from client import HybridLogicalClock

def main():
    print("=== Hybrid Logical Clock (HLC) Causality Coordinator ===")
    node1 = HybridLogicalClock("node1")
    node2 = HybridLogicalClock("node2")

    t1 = node1.now(physical_time=100)
    print("Node 1 Event:", t1)
    assert t1["l"] == 100
    assert t1["c"] == 0

    # Node 2 with lagging clock 95 receives message from node 1
    t2 = node2.update(t1["l"], t1["c"], physical_time=95)
    print("Node 2 Update:", t2)
    assert t2["l"] == 100
    assert t2["c"] == 1

    print("Hybrid Logical Clock verified successfully!")

if __name__ == "__main__":
    main()

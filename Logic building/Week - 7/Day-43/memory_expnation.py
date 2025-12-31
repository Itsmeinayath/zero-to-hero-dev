"""
Memory Management Demonstration: Call Stack in Action
======================================================

This file demonstrates how the call stack works during function calls.
Each function call creates a new "stack frame" in memory.

Run this file and observe:
1. Functions are called in order: print1 → print2 → print3 → print4
2. Each prints its number
3. The stack builds up (push phase)
4. Then unwinds back to main (pop phase)

Expected Output: 1 2 3 4
"""


def main():
    """
    Entry point. The main() frame is the first on the stack.
    """
    print("🚀 Starting call stack demonstration...")
    print("=" * 40)
    
    def print1(n):
        """
        Stack Frame 1 (Bottom of our call chain)
        - Parameter: n = 1
        - Action: Print 1, then call print2()
        - This frame waits (paused) until print2() returns
        """
        print(f"📍 print1 called with n={n}")
        print2(n=2)  # This pushes a new frame onto the stack
        print(f"✅ print1 resuming after print2 returned")
    
    def print2(n):
        """
        Stack Frame 2
        - Parameter: n = 2
        - Action: Print 2, then call print3()
        - This frame waits (paused) until print3() returns
        """
        print(f"📍 print2 called with n={n}")
        print3(n=3)  # This pushes a new frame onto the stack
        print(f"✅ print2 resuming after print3 returned")
    
    def print3(n):
        """
        Stack Frame 3
        - Parameter: n = 3
        - Action: Print 3, then call print4()
        - This frame waits (paused) until print4() returns
        """
        print(f"📍 print3 called with n={n}")
        print4(n=4)  # This pushes a new frame onto the stack
        print(f"✅ print3 resuming after print4 returned")
    
    def print4(n):
        """
        Stack Frame 4 (Top of our call chain - Maximum depth!)
        - Parameter: n = 4
        - Action: Print 4, then RETURN (no more calls!)
        - This is like a "base case" - it doesn't call anyone else
        """
        print(f"📍 print4 called with n={n}")
        print(f"🎯 Reached maximum depth! Starting to return...")
    
    # Start the chain reaction!
    print1(n=1)
    
    print("=" * 40)
    print("✨ All functions returned! Stack is empty.")


if __name__ == "__main__":
    main()
    
    print("\n" + "=" * 40)
    print("📚 MEMORY VISUALIZATION:")
    print("=" * 40)
    print("""
    Stack Growth (Push Phase):
    ┌──────────────┐
    │  print4(4)   │ ← Stack Pointer (top)
    ├──────────────┤
    │  print3(3)   │ ← Paused
    ├──────────────┤
    │  print2(2)   │ ← Paused
    ├──────────────┤
    │  print1(1)   │ ← Paused
    ├──────────────┤
    │  main()      │ ← Bottom
    └──────────────┘
    
    Stack Unwinding (Pop Phase):
    print4 returns → pop frame
    print3 resumes & returns → pop frame
    print2 resumes & returns → pop frame
    print1 resumes & returns → pop frame
    main resumes & exits
    
    Space Complexity: O(4) = O(N) where N = depth
    Each frame uses ~32-64 bytes of stack memory
    """)

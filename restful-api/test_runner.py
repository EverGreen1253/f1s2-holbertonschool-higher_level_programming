#!/usr/bin/env python3

def test_functions(functions):
    """Test all functions."""
    total = 0
    fail = 0
    ok = 0
    for func in functions:
        try:
            print(f"{func.__doc__}: ", end='') 
            func()
            print("OK")
            ok += 1
        except AssertionError as e:
            print(f"FAIL - {e}")
            fail += 1
        total += 1
    print(f"Total tests: {total}, OK: {ok}, FAIL: {fail}")
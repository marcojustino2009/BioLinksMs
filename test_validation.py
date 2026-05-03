#!/usr/bin/env python
"""Test validation script for FASE 6"""
import sys
sys.path.insert(0, '.')

print("=" * 50)
print("FASE 6 - VALIDATION TESTS")
print("=" * 50)

# Test 1: redis module (safe import)
try:
    import redis as redis_module
    print("✅ Test 1: redis module - OK")
except Exception as e:
    print(f"❌ Test 1: redis module - FAILED: {e}")
    redis_module = None

# Test 2: cache module  
try:
    from app.cache import init_redis, get_redis, REDIS_AVAILABLE, is_redis_available
    print("✅ Test 2: cache module - OK")
    print(f"   REDIS_AVAILABLE: {REDIS_AVAILABLE}")
except Exception as e:
    print(f"❌ Test 2: cache module - FAILED: {e}")

# Test 3: auth routes
try:
    from app.routes.auth import router
    print("✅ Test 3: auth routes - OK")
except Exception as e:
    print(f"❌ Test 3: auth routes - FAILED: {e}")

# Test 4: main app
try:
    from app.main import app
    print("✅ Test 4: main app - OK")
except Exception as e:
    print(f"❌ Test 4: main app - FAILED: {e}")

print("=" * 50)
print("VALIDATION COMPLETE")
print("=" * 50)

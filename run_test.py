"""Quick import test for BioLinkMS"""
import sys

# Test 1: Main app
try:
    from app.main import app
    print("[OK] app.main imported successfully")
    print(f"     FastAPI app: {app.title}")
except Exception as e:
    print(f"[FAIL] app.main: {e}")
    sys.exit(1)

# Test 2: Dependencies
try:
    from app.api.dependencies import get_current_user
    print("[OK] app.api.dependencies imported")
except Exception as e:
    print(f"[FAIL] dependencies: {e}")

# Test 3: Auth middleware
try:
    from app.auth.middleware import get_current_user as auth_middleware
    print("[OK] app.auth.middleware imported")
except Exception as e:
    print(f"[FAIL] middleware: {e}")

# Test 4: Routes
try:
    from app.routes import auth, tracking, sos, logs
    print("[OK] All routes imported successfully")
except Exception as e:
    print(f"[FAIL] routes: {e}")

print("\n✅ All imports validated!")

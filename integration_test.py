#!/usr/bin/env python3
"""
Integration test script to verify both ANPR and Chatbot functionalities can coexist.
"""

def test_chatbot_imports():
    """Test that chatbot modules can be imported successfully."""
    try:
        from sanjay_knowledge_base import get_knowledge_base, search_knowledge
        from sanjay_chatbot import create_chatbot
        print("✅ Chatbot modules import successfully")
        return True
    except Exception as e:
        print(f"❌ Chatbot import error: {e}")
        return False

def test_anpr_imports():
    """Test that ANPR modules can be imported (may require additional dependencies)."""
    try:
        import util
        print("✅ ANPR util module imports successfully")
        return True
    except Exception as e:
        print(f"❌ ANPR import error: {e}")
        print("   Note: This may require installing additional dependencies from requirements.txt")
        return False

def test_knowledge_base():
    """Test knowledge base functionality."""
    try:
        from sanjay_knowledge_base import get_knowledge_base, search_knowledge
        
        kb = get_knowledge_base()
        assert len(kb) > 0, "Knowledge base should not be empty"
        
        results = search_knowledge(["machine", "learning"])
        assert isinstance(results, dict), "Search should return a dictionary"
        
        print("✅ Knowledge base functionality works")
        return True
    except Exception as e:
        print(f"❌ Knowledge base test error: {e}")
        return False

def test_file_structure():
    """Test that all required files exist."""
    import os
    
    required_files = [
        'sanjay_knowledge_base.py',
        'sanjay_chatbot.py', 
        'chatbot_cli.py',
        'demo_chatbot.py',
        'CHATBOT_CONFIG.md',
        'requirements.txt',
        'README.md'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    else:
        print("✅ All required files exist")
        return True

def main():
    """Run integration tests."""
    print("🧪 Integration Test Suite")
    print("=" * 50)
    
    tests = [
        ("File Structure", test_file_structure),
        ("Chatbot Imports", test_chatbot_imports),
        ("Knowledge Base", test_knowledge_base),
        ("ANPR Imports", test_anpr_imports),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Testing {test_name}...")
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"❌ {test_name} failed with exception: {e}")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Integration successful.")
    else:
        print("⚠️  Some tests failed, but this may be due to missing optional dependencies.")
    
    print("\n💡 Next Steps:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Set API key: export ANTHROPIC_API_KEY='your-key'")
    print("3. Test chatbot: python chatbot_cli.py --topics")
    print("4. Run ANPR (if dependencies installed): python main.py")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""Test script to verify duke-agents can be imported correctly."""

import sys
import os

# Add src to path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    # Test basic imports
    print("Testing basic imports...")
    from duke_agents import AtomicAgent, CodeActAgent, Orchestrator, ContextManager
    print("✓ Basic imports successful")
    
    # Test model imports  
    print("\nTesting model imports...")
    from duke_agents.models import WorkflowMemory, AtomicInput, AtomicOutput, CodeActInput, CodeActOutput
    print("✓ Model imports successful")
    
    # Test configuration
    print("\nTesting configuration...")
    from duke_agents.config import Config
    print(f"✓ Config loaded, MISTRAL_MODEL = {Config.MISTRAL_MODEL}")
    
    # Test creating instances (without running)
    print("\nTesting instance creation...")
    context = ContextManager("Test import")
    print("✓ ContextManager created")
    
    agent = AtomicAgent("test_agent")  
    print("✓ AtomicAgent created")
    
    print("\n✅ All imports and basic instantiation successful!")
    print("\nPackage structure verified:")
    print("- Core classes importable from duke_agents")
    print("- Models importable from duke_agents.models")
    print("- Configuration system working")
    print("- Basic instantiation working")
    
except ImportError as e:
    print(f"\n❌ Import error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"\n❌ Error: {type(e).__name__}: {e}")
    sys.exit(1)
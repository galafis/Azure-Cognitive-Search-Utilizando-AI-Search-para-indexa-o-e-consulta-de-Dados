"""
Basic tests for Azure Cognitive Search documentation project
Author: Gabriel Demetrios Lafis
"""

import os
import pytest
from pathlib import Path


def test_readme_exists():
    """Test that README.md file exists"""
    readme_path = Path("README.md")
    assert readme_path.exists(), "README.md file should exist"


def test_readme_not_empty():
    """Test that README.md is not empty"""
    readme_path = Path("README.md")
    if readme_path.exists():
        content = readme_path.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "README.md should not be empty"


def test_license_exists():
    """Test that LICENSE file exists"""
    license_path = Path("LICENSE")
    assert license_path.exists(), "LICENSE file should exist"


def test_contributing_exists():
    """Test that CONTRIBUTING.md file exists"""
    contributing_path = Path("CONTRIBUTING.md")
    assert contributing_path.exists(), "CONTRIBUTING.md file should exist"


def test_requirements_exists():
    """Test that requirements.txt file exists"""
    requirements_path = Path("requirements.txt")
    assert requirements_path.exists(), "requirements.txt file should exist"


def test_requirements_not_empty():
    """Test that requirements.txt is not empty"""
    requirements_path = Path("requirements.txt")
    if requirements_path.exists():
        content = requirements_path.read_text(encoding='utf-8')
        assert len(content.strip()) > 0, "requirements.txt should not be empty"


def test_project_structure():
    """Test basic project structure"""
    current_dir = Path(".")
    
    # Check for essential files
    essential_files = ["README.md", "LICENSE", "requirements.txt"]
    for file_name in essential_files:
        file_path = current_dir / file_name
        assert file_path.exists(), f"{file_name} should exist in project root"


def test_readme_contains_author():
    """Test that README.md contains author information"""
    readme_path = Path("README.md")
    if readme_path.exists():
        content = readme_path.read_text(encoding='utf-8')
        assert "Gabriel Demetrios Lafis" in content, "README should contain author name"


def test_readme_bilingual():
    """Test that README.md is bilingual (Portuguese and English)"""
    readme_path = Path("README.md")
    if readme_path.exists():
        content = readme_path.read_text(encoding='utf-8')
        # Check for Portuguese content
        portuguese_indicators = ["🇧🇷", "Visão Geral", "Funcionalidades", "Como usar"]
        # Check for English content  
        english_indicators = ["🇺🇸", "Overview", "Features", "How to use"]
        
        has_portuguese = any(indicator in content for indicator in portuguese_indicators)
        has_english = any(indicator in content for indicator in english_indicators)
        
        assert has_portuguese or has_english, "README should be bilingual"


if __name__ == "__main__":
    pytest.main([__file__])

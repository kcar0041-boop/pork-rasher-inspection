import pytest
from src.labelling import derive_pass_fail

def test_no_defects_passes():
    """Test that an empty list of defects results in 'pass'."""
    assert derive_pass_fail([]) == 'pass'

def test_cosmetic_defect_passes():
    """Test that only a cosmetic defect ('wrinkle') results in 'pass'."""
    assert derive_pass_fail(['wrinkle']) == 'pass'
    assert derive_pass_fail(['wrinkle', 'minor_scuff']) == 'pass'

def test_fail_worthy_defect_fails():
    """Test that a single fail-worthy defect results in 'fail'."""
    assert derive_pass_fail(['loose_meat']) == 'fail'
    assert derive_pass_fail(['twisted_meat']) == 'fail'
    assert derive_pass_fail(['unsealed_packaging']) == 'fail'

def test_mixed_defects_fail_worthy_overrides():
    """Test that a mix of cosmetic and fail-worthy defects results in 'fail'."""
    assert derive_pass_fail(['wrinkle', 'loose_meat']) == 'fail'
    assert derive_pass_fail(['twisted_meat', 'minor_dent']) == 'fail'

def test_multiple_fail_worthy_defects_fails():
    """Test that multiple fail-worthy defects results in 'fail'."""
    assert derive_pass_fail(['loose_meat', 'unsealed_packaging']) == 'fail'

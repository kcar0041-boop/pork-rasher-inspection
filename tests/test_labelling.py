import pytest
from src.labelling import derive_pass_fail


def test_no_defects_passes():
    """No detected defects should pass."""
    assert derive_pass_fail([]) == "pass"


def test_cosmetic_defect_passes():
    """A wrinkle alone is cosmetic and should pass."""
    assert derive_pass_fail(["wrinkle"]) == "pass"


def test_fail_worthy_defect_fails():
    """A fail-worthy defect should fail."""
    assert derive_pass_fail(["loose-meat"]) == "fail"


def test_mixed_defects_fail_worthy_overrides():
    """A fail-worthy defect overrides a cosmetic one."""
    assert derive_pass_fail(["wrinkle", "twisted-meat"]) == "fail"


def test_multiple_fail_worthy_defects_fails():
    """Multiple fail-worthy defects should fail."""
    assert derive_pass_fail(["loose-meat", "unsealed", "packaging-error"]) == "fail"

import pytest
from src.labelling import derive_pass_fail


def test_no_defects_passes():
    assert derive_pass_fail([]) == "pass"


def test_cosmetic_defect_passes():
    assert derive_pass_fail(["wrinkle"]) == "pass"


def test_fail_worthy_defect_fails():
    assert derive_pass_fail(["loose_meat"]) == "fail"
    assert derive_pass_fail(["twisted_meat"]) == "fail"
    assert derive_pass_fail(["unsealed_packaging"]) == "fail"


def test_mixed_defects_fail_worthy_overrides():
    assert derive_pass_fail(["wrinkle", "loose_meat"]) == "fail"


def test_multiple_fail_worthy_defects_fails():
    assert derive_pass_fail(["loose_meat", "unsealed_packaging"]) == "fail"

import pytest
from src.labelling import derive_pass_fail


def test_no_defects_passes():
    assert derive_pass_fail([]) == "pass"


def test_cosmetic_defect_passes():
    assert derive_pass_fail(["wrinkle"]) == "pass"


def test_fail_worthy_defects_fail():
    assert derive_pass_fail(["loose-meat"]) == "fail"
    assert derive_pass_fail(["twisted-meat"]) == "fail"
    assert derive_pass_fail(["unsealed"]) == "fail"
    assert derive_pass_fail(["packaging-error"]) == "fail"


def test_mixed_defects_fail_worthy_overrides():
    assert derive_pass_fail(["wrinkle", "loose-meat"]) == "fail"


def test_multiple_fail_worthy_defects_fails():
    assert derive_pass_fail(["loose-meat", "unsealed"]) == "fail"

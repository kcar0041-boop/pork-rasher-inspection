"""Module for deriving pass/fail status from pork rasher defect classes."""

FAIL_WORTHY_DEFECTS = ["loose_meat", "twisted_meat", "unsealed_packaging"]


def derive_pass_fail(defect_class_names: list) -> str:
    """Derives a 'pass' or 'fail' status from a list of detected defect classes.

    Args:
        defect_class_names: List of defect class name strings detected in an image.

    Returns:
        'fail' if any fail-worthy defect is present, 'pass' otherwise.
        Cosmetic-only defects (e.g. 'wrinkle') do not cause a fail on their own.
    """
    for defect in defect_class_names:
        if defect in FAIL_WORTHY_DEFECTS:
            return "fail"
    return "pass"

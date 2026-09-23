"""Module for deriving pass/fail status from pork rasher defect classes."""

FAIL_WORTHY_DEFECTS = ["loose-meat", "twisted-meat", "unsealed", "packaging-error"]

def derive_pass_fail(defect_class_names: list) -> str:
    """Derives a 'pass' or 'fail' status from a list of detected defect classes.

    Args:
        defect_class_names: List of defect class name strings detected in an image.

    Returns:
        'fail' if any fail-worthy defect is present, 'pass' otherwise.
        'wrinkle' is treated as cosmetic-only and does not cause a fail on its own.
    """
    for defect in defect_class_names:
        if defect in FAIL_WORTHY_DEFECTS:
            return "fail"
    return "pass"

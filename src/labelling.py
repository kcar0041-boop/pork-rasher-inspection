"""Module for labelling pork rasher defects based on defect class names."""

def derive_pass_fail(defect_class_names: list) -> str:
    """Derives a 'pass' or 'fail' status based on a list of defect class names.

    Args:
        defect_class_names (list): A list of strings, where each string is a defect class name.

    Returns:
        str: 'fail' if any fail-worthy defect is present, 'pass' otherwise.
             'wrinkle' is considered cosmetic and does not result in a 'fail'.

    Fail-worthy defects include: 'loose_meat', 'twisted_meat', 'unsealed_packaging'.
    """
    fail_worthy_defects = ['loose_meat', 'twisted_meat', 'unsealed_packaging']

    for defect in defect_class_names:
        if defect in fail_worthy_defects:
            return 'fail'

    return 'pass'


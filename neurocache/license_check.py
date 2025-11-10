def verify_license(key: str) -> bool:
    VALID_KEYS = {"DEMO-123", "FREE-EDU"}
    if key in VALID_KEYS:
        return True
    raise PermissionError("Commercial license required. Contact nicole.assenza@outlook.com")


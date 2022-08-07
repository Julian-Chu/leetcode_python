def ParseInt(s: str) -> bool:
    try:
        num = int(s)
        return True
    except ValueError:
        return False
    except Exception:
        return False

def repeatedSubstringPattern(s: str) -> bool:
    s_len = len(list(s))
    for i in range(1, (s_len // 2) + 1):
        if s_len != 1 and s[:i] * (s_len // i) == s:
            return True
    else:
        return False


if __name__ == "__main__":
    # Repeated Substring Pattern
    s = "abcabc"
    print(repeatedSubstringPattern(s))

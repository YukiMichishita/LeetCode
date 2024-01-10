from typing import List


def regularize_email_address(address: str) -> str:
    local = ""
    domain = ""
    is_domain = False
    is_alias = False
    for c in address:
        if c == "@":
            is_domain = True
            continue
        if is_domain:
            domain += c
        else:
            if c == ".":
                continue
            if c == "+":
                is_alias = True
            if is_alias:
                continue
            local += c
    return f'{local}@{domain}'


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        regularized_emails = set()
        for email in emails:
            regularized_emails.add(regularize_email_address(email))
        return len(regularized_emails)

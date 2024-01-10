from typing import List, Optional
import re


def regularize_email_address(address: str) -> Optional[str]:
    email_address_ptn = r"([\w\.]+)(\+[\w\.\+]+)?@([\w\.\+]+)"
    match = re.match(email_address_ptn, address)

    if not match:
        return ""
    return f"{match.group(1).replace('.', '')}@{match.group(3)}"


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        regularized_emails = set()
        for email in emails:
            r = regularize_email_address(email)
            if r:
                regularized_emails.add(r)
        return len(regularized_emails)

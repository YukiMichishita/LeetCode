from typing import List


def email_address_to_send(email: str) -> str:
    local, domain = email.split("@", 2)
    local = local.split("+")[0]
    local = local.replace(".", "")
    return f"{local}@{domain}"


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            unique_emails.add(email_address_to_send(email))
        return len(unique_emails)

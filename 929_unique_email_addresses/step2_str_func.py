from typing import List


def regularize_email_address(address: str):
    local, domain = address.split("@", 2)
    local = local.split("+")[0]
    local = local.replace(".", "")

    return f'{local}@{domain}'


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        regularized_unique_emails = set()
        for email in emails:
            regularized_unique_emails.add(regularize_email_address(email))

        return len(regularized_unique_emails)

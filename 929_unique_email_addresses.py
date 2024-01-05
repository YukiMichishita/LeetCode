from typing import List


def get_email_address_to_send(email: str):
    local, domain = email.split("@")
    local = local.split("+")[0]
    local = local.replace(".", "")

    return local + "@" + domain


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        regularized_emails = []
        for email in emails:
            regularized_emails.append(get_email_address_to_send(email))

        print(regularized_emails)
        return len(set(regularized_emails))

# emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# s = Solution()
# print(s.numUniqueEmails(emails))

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        for email in emails:
            local,domain = email.split('@')

            local = local.split('+')[0]
            local = local.replace('.','')

            cleanEmail = local+'@'+domain
            uniqueEmails.add(cleanEmail)
        return len(uniqueEmails)
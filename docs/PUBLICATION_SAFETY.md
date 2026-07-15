# Publication safety

The original legacy study-note directory was removed after migration. Its historical path remains
Git-ignored so it cannot be accidentally recreated and published. Any future private source
material requires human privacy and confidentiality review before an idea can be generalized.

Before staging or pushing content:

1. Confirm the material is original and that you have the right to publish it.
2. Remove employer and client names, internal system names, private architecture, proprietary metrics, and confidential interview questions.
3. Remove personal information, credentials, internal links, real identifiers, customer information, and protected health information.
4. Replace examples with fictional, synthetic, employer-neutral data.
5. Search staged files for secrets, email addresses, employer names, and privacy-sensitive terms.
6. Keep private redaction terms only in `backups/private_terms.txt`, which is Git-ignored; never
   hardcode a private employer list in public migration code.
7. Inspect `git diff --cached` manually before committing.

When uncertain, do not publish the material.

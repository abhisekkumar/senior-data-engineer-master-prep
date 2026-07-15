# Publication safety

The legacy study-note directory is intentionally Git-ignored and must remain local. It contains material that requires human privacy and confidentiality review before any idea can be generalized for publication.

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

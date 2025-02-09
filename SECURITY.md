# Security Policy

## Supported Versions

This section outlines the supported versions of the ML Project Template that receive security updates.  Due to the nature of this project as a template, security updates primarily focus on the template's code itself (e.g., the `create_project.py` script) and the dependencies it utilizes.  Projects generated *from* this template are the responsibility of the individual project owners to secure.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| v1.x.x  | :white_check_mark: |  Active development and security updates.  Recommended for new projects. |
| v0.x.x  | :x: | No longer supported.  Upgrade to the latest v1.x.x release for security updates. |


## Reporting a Vulnerability

We take the security of the ML Project Template seriously.  If you discover a potential vulnerability, please report it responsibly.

**How to Report:**

1.  **Do not publicly disclose the vulnerability** until we have had a chance to address it.
2.  Create a new issue on the GitHub repository: [https://github.com/BodieCoding/ml-project-template/issues](https://github.com/BodieCoding/ml-project-template/issues).
3.  Provide as much detail as possible about the vulnerability, including:
    *   The specific version of the template affected.
    *   A clear description of the vulnerability.
    *   Steps to reproduce the vulnerability.
    *   Any potential impact of the vulnerability.

**Response Process:**

1.  We will acknowledge your report within **72 hours** (typically much sooner).
2.  We will investigate the vulnerability and determine its severity.
3.  We will provide updates on the progress of the investigation and any planned fixes.
4.  If the vulnerability is confirmed, we will release a patch as soon as possible.  We aim for a rapid response, typically within **one week** for critical vulnerabilities.
5.  We will notify you when the patch is released.

**Vulnerability Acceptance/Decline:**

*   If the reported issue is confirmed as a security vulnerability, we will address it as described above.
*   If the reported issue is not a security vulnerability (e.g., a bug, a feature request, or a misunderstanding), we will explain our reasoning and may close the issue.  We appreciate all reports and will provide feedback even if the issue is not a vulnerability.

**Important Note Regarding Generated Projects:**

This security policy applies to the ML Project Template itself.  Projects generated using this template inherit the security posture of the template at the time of creation.  It is the responsibility of the developers of those individual projects to ensure their ongoing security.  This includes:

*   Regularly updating dependencies.
*   Implementing appropriate security measures within their project code.
*   Conducting their own security audits and vulnerability assessments.

We strongly recommend that projects generated from this template adopt their own security policies and procedures.

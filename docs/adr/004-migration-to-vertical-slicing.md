## Architecture Decision Record 16/03/2026
Migration to Vertical Slicing Architecture Explanation

It was decided to migrate to a Vertical Slicing architecture because, as new services and folders were added, navigating the project became increasingly difficult. Additionally, this new arrangement helps prevent coupling between different SOAP services that are not related to each other in any way.

Now all utilities for a given service are contained within an exclusive folder for that service, with the exception of general utilities which are located in a /shared folder. This improves the project's scalability and prevents it from becoming confusing to understand. Furthermore, it allows teams to work on a single service without the risk of affecting and/or breaking other parts of the software when making modifications.

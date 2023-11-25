
# Environment Variables Management

This document outlines the approach for managing environment variables in the `diopticon` project, ensuring compatibility across local development, CI/CD pipelines, and Streamlit Community Hosting.

## Local Development

- Environment variables are loaded from a `.env` file using `dotenv`.
- This file is only used locally and is excluded from version control.
- Example snippet from `app/main.py`:
  
  ```python
  if os.path.exists('.env'):
      from dotenv import load_dotenv
      load_dotenv()
  ```

## CI/CD Pipeline (GitHub Actions)

- Environment variables are set in the GitHub repository settings under 'Secrets'.
- These are then passed to the GitHub Actions workflows.
- The workflow uses these secrets to set environment variables during the build and deployment process.

## Streamlit Community Hosting

- Environment variables are configured in the Streamlit interface under 'Advanced settings'.
- These settings allow for secure entry of sensitive information, separate from the codebase.

## Purpose of Environment Variables

- `DB_DIOPTICON_S`, `DB_DIOPTICON_D`, `DB_DIOPTICON_U`, `DB_DIOPTICON_P`: Used for configuring the connection to the Diopticon database. This contains the content of the specific app implementation.
- `DB_DIS_S`, `DB_DIS_D`, `DB_DIS_U`, `DB_DIS_P`: Used for connecting to an additional database, if applicable.
- `OPENAI_API`: Stores the API key for accessing OpenAI services.

## Best Practices

- Environment variables should never be hard-coded or committed to version control.
- Ensure consistency in naming and usage across all environments.
- Use secure methods to set and access these variables in production and hosted environments.

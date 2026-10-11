# EKO-FTP-upload

Upload EKO MS711/MS711-DNI spectroradiometer measurements to FTP (creating monthly folders). 

Archives files older than current day to local directory adding prefix to basename.

### Setup

The same repo runs on both NUCs. Per-instrument settings (FTP folder, file prefix, local data folder) are in `config.json`.

In `cmd`, in the repo folder:

```
pip install python-dotenv
copy .env.example .env
notepad .env
```

Set the real values in `.env`, replacing the placeholders. `INSTRUMENT` is `ms711` or `ms711-dni`. `.env` is in `.gitignore`.

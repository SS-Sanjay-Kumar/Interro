# Interro

**Interro** is an AI-powered learning assessment tool that generates questions strictly from the material you study.

Upload PDFs, YouTube videos, or web resources, and Interro analyzes the content to ask context-aware questions—helping you test real understanding instead of memorization.

Built to solve a problem I faced personally: knowing whether I truly learned something, not just consumed it.

Completed so far:

- [x] url-ingest-service : get resourceURL from the user, get it using httpx and extract only the text content using bs4
- [x] yt-transcript-service : get youtube video id from the user, get the transcript using yt-transcript-api
- [x] handling pdf uploads using multer and save it locally in uploads/ folder.
- [x] extract text content from the uploaded pdf and also auto delete it after.

IMPORTANT:
 - Instead of having nodejs and express as backend, choosing fastapi/flask (or any python based frameworks) would make a lot more sense.
   > So go with fastapi, refactor everything

PRIORITY Need to do:

- [ ] feed all 3 of the data to AI
- [ ] refactor the code to improve its quality
- [ ] add support for a handful to file types such as doc, txt etc...
- [ ] extract tablular data, images etc from files  

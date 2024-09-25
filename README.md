# mksld

A very crappy (dockerized) script written in 10ish mins that scrapes [@MKBHD](https://x.com/MKBHD)'s wallpaper app's (Panels) **public** API and fetches all the images tagged with `dhd` (high-definition image).

> [!NOTE]
> I own none of the content fetched by this script. All rights go to their respective copyright holders.

## Usage

Python 3 + dependencies:
```sh
python3 src/mksld.py
```

Docker:
```sh
./docker-run.sh
```

## Credit
- [@uwukko](https://x.com/uwukko/status/1838640932167503998) for posting about the media API endpoint.
- [@grok](https://x.com/grok) for boiler-plate element traversal with `requests`.

## Production

```bash
docker image build -t hacker-news-scrapper .
```

```bash
docker run -d -p 5000:5000 hacker-news-scrapper
```

## Development

### Execute

```bash
docker-compose -f ./docker-compose.dev.yml up --build
```

Then visit:

```
http://0.0.0.0:5000
```

### Shutdown

Focus the terminal where the session is running and excute `Ctrl + C`.
Then execute:

```bash
docker-compose -f ./docker-compose.dev.yml down
```

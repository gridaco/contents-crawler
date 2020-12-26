# Classified Text Crawler
- This directory is a scrapy project, containing spiders for extracting text from buttons, inputs, and etc.
- It uses domains from `ALLOWLIST` to start crawling. Each page is crawled until it reaches the depth in `DOMAIN_DEPTHS` in settings(if it's not specified, it follows `DEPTH_LIMIT`. Default is 5). To implement this, the `DomainDepthMiddleware` is used(Please refer to middlewares).

## Spiders
The spiders are in the `classified_text_crawler/spiders` directory.

```bash
scrapy crawl button_crawler -o button_texts.jl
```

To run a specific spider, use the command above. the `.ji` file is where the output is stored. You can terminate the process to stop crawling and write the data collected.

All crawler follows all the links with the anchor tag(`a`).

## Button Crawler

### This crawler seaches for...
- `button`
- `a` with className `btn`, `button`, `Button`

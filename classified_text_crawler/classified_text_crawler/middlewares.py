import logging
import tldextract
from scrapy.http import Request

# https://stackoverflow.com/questions/27805952/scrapy-set-depth-limit-per-allowed-domains


class DomainDepthMiddleware(object):
    def __init__(self, domain_depths, default_depth):
        self.domain_depths = domain_depths
        self.default_depth = default_depth

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        domain_depths = settings.getdict('DOMAIN_DEPTHS', default={})
        default_depth = settings.getint('DEPTH_LIMIT', 1)

        return cls(domain_depths, default_depth)

    def process_spider_output(self, response, result, spider):
        def _filter(request):
            if isinstance(request, Request):
                # get max depth per domain
                domain = tldextract.extract(request.url).registered_domain
                maxdepth = self.domain_depths.get(domain, self.default_depth)

                depth = response.meta.get('depth', 0) + 1
                request.meta['depth'] = depth

                if maxdepth and depth > maxdepth:
                    logging.debug(
                        f"Ignoring link (depth > {maxdepth}): {request.url} ")
                    return False
            return True

        return (r for r in result or () if _filter(r))

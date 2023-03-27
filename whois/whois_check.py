from fastapi import FastAPI
import whois
from fastapi.middleware.cors import CORSMiddleware
# from prometheus_client import start_http_server, Counter, Info, Gauge,Histogram, MetricsHandler, make_asgi_app
from aioprometheus import Counter, Gauge, Histogram, Summary, MetricsMiddleware
from aioprometheus.asgi.starlette import metrics
import time
# app_metrics = make_asgi_app()
# start_http_server(port=8000)
c=Counter('whois_check_requests','Number of whois check requests')
# function execution time , type Histogram
h=Histogram('whois_check_execution_time','whois check execution time')
app = FastAPI()
# app.add_middleware(middleware_class=MetricsHandler, prefix="/metrics")
# app.add_route("/metrics", app_metrics)
app.state.users_events_counter = Counter("events", "Number of events.")

app.add_middleware(MetricsMiddleware)
app.add_route("/metrics", metrics)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/v1/availability")
async def av_check(domain: str):
    start=time.time()
    c.inc(labels={})
    w=''
    try:
        w = whois.whois(domain)
    except :
        pass
    import random
    time.sleep(random.randint(1, 5))
    end=time.time()
    response_time=end-start
    h.add({}, value=response_time)
    
    if isinstance(w, dict) and w.get('domain_name'):
        return {'domain':domain,'availability':'not available'}
    elif isinstance(w, dict) and not w.get('domain_name') :
        return {'domain':domain,'availability':'available'}
    else:
        return {'domain':domain,'availability':'available'}
        




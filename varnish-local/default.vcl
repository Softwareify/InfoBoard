vcl 4.1;

backend nginx_infoboard_cms {
    .host = "nginx-infoboard-cms";
    .port = "8082";
    .probe = {
        .url = "/health/health-check";
        .timeout = 2s;
        .interval = 5s;
        .window = 10;
        .threshold = 5;
   }
}

backend nginx_infoboard_front {
    .host = "nginx-infoboard-front";
    .port = "8081";
    .probe = {
        .url = "/health/health-check";
        .timeout = 2s;
        .interval = 5s;
        .window = 10;
        .threshold = 5;
   }
}

sub vcl_recv {
    if (req.method == "PURGEPATH") {
        ban("req.url ~ " + req.http.X-Purge-Path);
        return(synth(200, "Purged"));
    }

        if (req.method == "POST") {
            return (pass);
        }

    if (req.http.host == "cms.infoboard.pl") {
        set req.http.host = "cms.infoboard.pl";
        set req.backend_hint = nginx_infoboard_cms;
        return (pass);
    }

    if (req.http.host == "infoboard.pl") {
        set req.http.host = "infoboard.pl";
        unset req.http.Authorization;
        unset req.http.Cookie;
        set req.backend_hint = nginx_infoboard_front;
    }

        if (req.url ~ "^[^?]*\.(jpeg|jpg|js|mp4|svg||webp)(\?.*)?$") {
            unset req.http.Cookie;
            unset req.http.Authorization;
        }
    }


sub vcl_backend_response {
    set beresp.ttl = 24h;
    set beresp.grace = 3d;
    set beresp.keep = 7d;
}
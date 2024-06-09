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
        # BAN SECTION
        if (req.http.X-Forwarded-For && req.method == "FULLBAN" || req.method == "PURGEBOTH" || req.method == "PURGEPATH" || req.method == "PURGEHOST") {

            # Ban everything
            if (req.method == "FULLBAN") {
                ban("obj.status != 0");
                return (synth(200, "Full cache cleared"));
            }

            # Ban based on domain (X-Purge-Domain) and path (X-Purge-Path)
            if (req.method == "PURGEBOTH") {
                ban("req.http.host ~ ^" + req.http.X-Purge-Domain + " && req.url ~ " + req.http.X-Purge-Path);
                return(synth(200, "Purged"));
            }

            # Ban based on domain (X-Purge-Domain)
            if (req.method == "PURGEHOST") {
                ban("req.http.host ~ ^" + req.http.X-Purge-Domain);
                return(synth(200, "Purged"));
            }

            # Ban based on path (X-Purge-Path)
            if (req.method == "PURGEPATH") {
                ban("req.url ~ " + req.http.X-Purge-Path);
                return(synth(200, "Purged"));
            }
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

        if (req.url ~ "^[^?]*\.(7z|avi|bmp|bz2|css|csv|doc|docx|eot|flac|flv|gif|gz|ico|jpeg|jpg|js|less|mka|mkv|mov|mp3|mp4|mpeg|mpg|odt|ogg|ogm|opus|otf|pdf|png|ppt|pptx|rar|rtf|svg|svgz|swf|tar|tbz|tgz|ttf|txt|txz|wav|webm|webp|woff|woff2|xls|xlsx|xml|xz|zip)(\?.*)?$") {
            unset req.http.Cookie;
            unset req.http.Authorization;
        }
    }


sub vcl_backend_response {
    set beresp.ttl = 24h;
    set beresp.grace = 3d;
    set beresp.keep = 7d;

    if (bereq.url ~ "^[^?]*\.(7z|avi|bmp|bz2|css|csv|doc|docx|eot|flac|flv|gif|gz|ico|jpeg|jpg|js|less|mka|mkv|mov|mp3|mp4|mpeg|mpg|odt|ogg|ogm|opus|otf|pdf|png|ppt|pptx|rar|rtf|svg|svgz|swf|tar|tbz|tgz|ttf|txt|txz|wav|webm|webp|woff|woff2|xls|xlsx|xml|xz|zip)(\?.*)?$") {
        unset beresp.http.Set-Cookie;
        set beresp.ttl = 24h;
    }
}
vcl 4.1;

backend nginx_infoboard_cms {
    .host = "nginx_infoboard_cms";
    .port = "8082";
}

backend nginx_infoboard_front {
    .host = "nginx_infoboard_front";
    .port = "8081";
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

        if (req.http.host == "cms.infoboard-local.wronamichal.pl") {
            set req.http.host = "cms.infoboard-local.wronamichal.pl";
            set req.backend_hint = nginx_infoboard_cms;
            return (pass);
        } elsif (req.http.host == "infoboard-local.wronamichal.pl") {
            set req.http.host = "infoboard-local.wronamichal.pl";
            set req.backend_hint = nginx_infoboard_front;
        } else {
            return(synth(500));
        }

        if (req.url ~ "^[^?]*\.(7z|avi|bmp|bz2|css|csv|doc|docx|eot|flac|flv|gif|gz|ico|jpeg|jpg|js|less|mka|mkv|mov|mp3|mp4|mpeg|mpg|odt|ogg|ogm|opus|otf|pdf|png|ppt|pptx|rar|rtf|svg|svgz|swf|tar|tbz|tgz|ttf|txt|txz|wav|webm|webp|woff|woff2|xls|xlsx|xml|xz|zip)(\?.*)?$") {
            unset req.http.Cookie;
            unset req.http.Authorization;
            return(hash);
        }
        if (req.method != "POST") {
            return (pass);
        }
    }


sub vcl_backend_response {
    if (bereq.url ~ "^[^?]*\.(7z|avi|bmp|bz2|css|csv|doc|docx|eot|flac|flv|gif|gz|ico|jpeg|jpg|js|less|mka|mkv|mov|mp3|mp4|mpeg|mpg|odt|ogg|ogm|opus|otf|pdf|png|ppt|pptx|rar|rtf|svg|svgz|swf|tar|tbz|tgz|ttf|txt|txz|wav|webm|webp|woff|woff2|xls|xlsx|xml|xz|zip)(\?.*)?$") {
        unset beresp.http.Set-Cookie;
        set beresp.ttl = 1d;
    }
}